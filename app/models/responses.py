from pydantic import BaseModel
from typing import Optional

class HealthResponse(BaseModel):
    transcription: str
    summary: str
    didctarized: str
    keyWords: Optional[str]
    actionPoints: Optional[str]