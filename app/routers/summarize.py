from fastapi import APIRouter, Depends, File, UploadFile

from app.models.responses import HealthResponse
from app.services.summarize import transcribe_and_summarize
from app.services.auth import verify_jwt

router = APIRouter(prefix="/summarize", tags=["Summarize"])

@router.post("/health", response_model=HealthResponse, status_code=200)
async def health_response(audio: UploadFile = File(...), payload=Depends(verify_jwt)):
    """
    Recebe um áudio, transcreve com Whisper, resume com ChatGPT baseado no tipo `health`.
    """

    response = await transcribe_and_summarize(audio, "health")

    return response

    
    
    