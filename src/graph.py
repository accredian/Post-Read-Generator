from agents import generate_queries, search_web, write_section
from state import SectionState, SectionOutputState
from langgraph.graph import START, END, StateGraph
from IPython.display import Image, display
from prompts import report_planner_instructions, report_planner_query_writer_instructions, report_structure
from agents import generate_report_plan
from state import Section, SectionState,ReportState
from IPython.display import Markdown
from rich.console import Console
from rich.markdown import Markdown

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

# View
display(Image(section_builder_graph.get_graph(xray=1).draw_mermaid_png()))



# Tavily search parameters
tavily_topic = "general"
tavily_days = None # Only applicable for news topic
# Topic 
report_topic = "Machine Learning."
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



    # Initialize the console
    console = Console()

    # Display markdown content
    for section in completed_sections:
        console.print(Markdown(f"## {section.name}"))
        console.print(Markdown(f"{section.content}"))

 
# Run the async function
res= asyncio.run(main())
asyncio.run(write_sections(res['sections']))