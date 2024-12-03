from pydantic import BaseModel, Field
from typing import Optional

class EmailInput(BaseModel):
    customer_id: int = Field(..., description="Unique identifier of the customer")
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Email body content")

class EmailOutput(BaseModel):
    customer_id: int = Field(..., description="Unique identifier of the customer")
    subject: str = Field(..., description="Email subject")
    category: str = Field(..., description="Classified category of the email")
    summary: str = Field(..., max_length=150, description="Summary of the email body")
    cvu: Optional[str] = Field(None, description="Extracted CVU if present")