from pydantic import BaseModel, Field
from typing import List, TypedDict


# Define the Section class
class SearchQuery(BaseModel):
    search_query: str = Field(
        None, description="Query for web search."
    )
class Queries(BaseModel):
    queries: List[SearchQuery] = Field(
        description="List of search queries.",
    )
class AgentState(TypedDict):
    topic: str
    query: List[str]
    search_results: List[str]
    report: str
    