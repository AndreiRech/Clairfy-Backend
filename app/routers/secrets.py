from fastapi import APIRouter, HTTPException, Header
from typing import List
from app.database.database import fetch_from_supabase
from app.services.service import check_token
from app.models.api import APIModel
from app.models.prompt_model import PromptModel

router = APIRouter(prefix="/secrets", tags=["secrets"])

@router.get("/api-key", response_model=APIModel, status_code=200)
async def get_api_key(x_token: str = Header(...)):
    """
    Retorna apenas a `api_key` presente na tabela `secure_data` do Supabase.

    - Protegido por token de acesso via header.
    - Útil para fornecer a chave de API à aplicação Swift de forma segura.
    """

    check_token(x_token)
    data = await fetch_from_supabase("secure_data")
    
    if not data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado na tabela 'secure_data'.")
    
    return {"api_key": data[0]["api_key"]}

@router.get("/prompts", response_model=List[PromptModel], status_code=200)
async def get_prompts(x_token: str = Header(...)):
    """
    Retorna uma lista de prompts disponíveis na tabela `prompts` do Supabase, 
    contendo apenas os campos: `prompt`, `type` e `category`.

    - Protegido por token de acesso via header.
    - Utilizado pela aplicação para exibir os prompts categorizados.
    """

    check_token(x_token)
    data = await fetch_from_supabase("prompts")
    
    if not data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado na tabela 'secure_data'.")

    return [
        {
            "prompt": d["prompt"],
            "type": d.get("type"),
            "category": d.get("category")
        }
        for d in data
    ]
