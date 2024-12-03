from pydantic import BaseModel, Field
from typing import Optional

class RAGQueryInput(BaseModel):
    query: str = Field(..., description="User's query text")

class RAGQueryOutput(BaseModel):
    answer: str = Field(..., description="Generated answer for the query")
    context: Optional[str] = Field(None, description="Relevant context retrieved for the query")