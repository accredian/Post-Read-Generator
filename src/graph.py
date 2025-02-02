from agents import generate_queries, search_web, write_section
from state import SectionState, SectionOutputState
from langgraph.graph import START, END, StateGraph
from IPython.display import Image, display
from prompts import report_structure
from agents import generate_report_plan, write_section
from state import SectionState
from IPython.display import Markdown
from rich.console import Console
from rich.markdown import Markdown
from md2docx_python.src.md2docx_python import markdown_to_word
import os, load_dotenv



# Load the environment variables
os.environ["NVIDIA_API_KEY"]="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"





# Add nodes and edges 
section_builder = StateGraph(SectionState, output=SectionOutputState)
section_builder.add_node("generate_queries", generate_queries)
section_builder.add_node("search_web", search_web)
section_builder.add_node("write_section", write_section)

section_builder.add_edge(START, "generate_queries")
section_builder.add_edge("generate_queries", "search_web")
section_builder.add_edge("search_web", "write_section")
section_builder.add_edge("write_section", END)

# Compile
section_builder_graph = section_builder.compile()




# Tavily search parameters
tavily_topic = "general"
tavily_days = None # Only applicable for news topic
# Topic 
report_topic = "Computer vision."
import asyncio

async def main():
    # Generate report plan
    sections = await generate_report_plan({"topic": report_topic, "report_structure": report_structure, "number_of_queries": 2, "tavily_topic": tavily_topic, "tavily_days": tavily_days})

    return sections


 # Loop through all sections and write each section
async def write_sections(sections):
    completed_sections = []
    for section in sections:
        if section.research:
            result = await section_builder_graph.ainvoke({
                "section": section,
                "number_of_queries": 2,
                "tavily_topic": tavily_topic,
                "tavily_days": tavily_days
            })
            completed_sections.extend(result["completed_sections"])
        else:
            result=write_section({"section": section, "source_str": ""})
            completed_sections.extend(result["completed_sections"])
   



    # Initialize the console
    console = Console()

    # # Display markdown content
    # for section in completed_sections:
    #     console.print(Markdown(f"## {section.name}"))
    #     console.print(Markdown(f"{section.content}"))
        
    with open("output/report.md", "w") as file:
        for section in completed_sections:
            file.write(f"## {section.name}")
            file.write("\n\n")
            file.write(f"{section.content}")
            file.write("\n\n")
        file.close()
    markdown_to_word("output/report.md", "output/report.docx")
 
# Run the async function
res= asyncio.run(main())
asyncio.run(write_sections(res['sections']))