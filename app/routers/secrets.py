from fastapi import APIRouter, Depends
from typing import List
from app.services.auth import verify_jwt
from app.models.api import APIModel
from app.models.prompt import PromptModel
from app.services.secrets import fetch_api_key, fetch_prompts

router = APIRouter(prefix="/secrets", tags=["Secrets"])

@router.get("/api-key", response_model=APIModel, status_code=200)
async def get_api_key(payload=Depends(verify_jwt)):
    """
    Retorna apenas a `api_key` presente na tabela `secure_data` do Supabase.
    """

    response = await fetch_api_key()
    
    return response

@router.get("/prompts", response_model=List[PromptModel], status_code=200)
async def get_prompts(payload=Depends(verify_jwt)):
    """
    Retorna uma lista de prompts disponíveis na tabela `prompts` do Supabase, 
    contendo apenas os campos: `prompt`, `type` e `category`.
    """

    response = await fetch_prompts()

    return response
