from pydantic import BaseModel, Field
from typing import Literal

class Task(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=500)
    status: Literal["pending", "Done"]