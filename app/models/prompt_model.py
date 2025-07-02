from pydantic import BaseModel
from typing import Optional

class PromptModel(BaseModel):
    prompt: str
    type: Optional[str]
    category: Optional[str]
    