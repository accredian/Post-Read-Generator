# Description: This file contains the implementation of the agents that will be used in the pipeline.
from typing import List
from langchain_core.messages import HumanMessage, SystemMessage
from prompts import query_template, report_prompt
from state import AgentState, Queries
import os, re
from dotenv import load_dotenv
from tavily import TavilyClient, AsyncTavilyClient
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from md2docx_python.src.md2docx_python import markdown_to_word
import streamlit as st



#############################################################################################################
# Query geneartive agent
def generate_queries(topic: str) -> List[str]:
    # Format system instructions
    system_instruction_query = query_template.format(topic=topic)
    # Generate queries
    structured_llm = llm.with_structured_output(Queries)
    result = structured_llm.invoke(
        [SystemMessage(content=system_instruction_query)]+
         [HumanMessage(content="Generate search queriesthat will help with planning the sections of the report.")]
        )
    return {'query':[i.search_query for i in result.queries]}


# 2. Web Search Agent
def perform_search(state: AgentState):
    results = []
    for query in state['query']:
        search_results = tavily_client.search(query,max_results=2)  # Get top 5 results per query
        results.append({
            "query": query,
            "results": [{
                "title": res["title"],
                "url": res["url"],
                "content": res["content"][:1000]  # Truncate for demo
            } for res in search_results['results']]
        })
    return {"search_results": results}


# Report generating agent
def report_generation(state: AgentState) -> str:
    # Extracting relevant search results from the state
    search_results = state['search_results']
    
    # Format system instructions
    formatted_results = "\n".join(
        [f"**{result['query']}**\n" + "\n".join(
            [f"- [{res['title']}]({res['url']}): {res['content']}" for res in result['results']]
        ) for result in search_results]
    )
    
    system_instruction = report_prompt + "\n\n" + formatted_results

    # Write report
    result = llm.invoke(
        [SystemMessage(content=system_instruction)] +
        [HumanMessage(content="Write a concise report using the above information.")]
    )

    # Return only the generated report text
    return {"report": result.content}




#############################################################################################################
# streamlit application

# Set the title of the app
st.title("Post read Report Generator Agent")

# Sidebar with API key input fields and a brief description
st.sidebar.title("API Keys and Description")
api_key_1 = st.sidebar.text_input("Tavily API Key 1", type="password")
api_key_2 = st.sidebar.text_input("Groq API Key 2", type="password")
st.sidebar.info("This is a Streamlit app that takes two API keys as input and allows users to enter a topic for processing.")

#######################################################################
# Set the API keys to environment variables
os.environ["TAVILY_API_KEY"] = api_key_1
os.environ["GROQ_API_KEY"] = api_key_2

# Proceed with model initialization
llm = ChatGroq(model="deepseek-r1-distill-llama-70b",verbose=False)

#Search client
tavily_client = TavilyClient()
tavily_async_client = AsyncTavilyClient()
#######################################################################


# Function to run the main app logic
def run_app(topic):
    # Placeholder logic to demonstrate usage
    st.write(f"Processing topic: {topic}")
    
    # Build LangGraph workflow
    workflow = StateGraph(AgentState)
    workflow.add_node("generate_queries", generate_queries)
    workflow.add_node("perform_search", perform_search)
    workflow.add_node("report_generation", report_generation)


    workflow.set_entry_point("generate_queries")
    workflow.add_edge("generate_queries", "perform_search")
    workflow.add_edge("perform_search", "report_generation")
    workflow.add_edge("report_generation",END)

    workflow_graph = workflow.compile()

    result=workflow_graph.invoke({"topic": topic})

    # Display the generated report
    st.markdown(re.sub(r'<think>.*?</think>\n\n', '', result['report'], flags=re.DOTALL))

    # save to markdown file
    with open('report.md', 'w') as f:
        f.write(re.sub(r'<think>.*?</think>\n\n', '', result['report'], flags=re.DOTALL))

    markdown_to_word('report.md', 'report.docx')
    st.success("Report generated successfully. Check the markdown and docx files for the report.")

     # Add download button
    with open("report.docx", "rb") as file:
        report_data = file.read()
        
    st.download_button(
        label="Download Report",
        data=report_data,
        file_name="report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Main screen input field for topic
topic = st.text_input("Enter the topic")

# Submit button to run the app
if st.button("Submit"):
    if api_key_1 and api_key_2 and topic:
        run_app(topic)
    else:
        st.error("Please enter both API keys and a topic.")
