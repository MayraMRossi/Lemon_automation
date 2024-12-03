from pydantic import BaseModel, Field
from typing import Optional

class IntentInput(BaseModel):
    question: str = Field(..., description="User's query text")

class IntentOutput(BaseModel):
    intent: str = Field(..., description="Predicted intent category")
    confidence: Optional[float] = Field(None, description="Confidence score of the prediction")