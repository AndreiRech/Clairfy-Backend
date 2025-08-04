from fastapi import HTTPException
from app.database.database import fetch_from_supabase
from app.models.api import APIModel
from app.models.prompt import PromptModel

async def fetch_api_key() -> APIModel:
    data = await fetch_from_supabase("secure_data")

    if not data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado na tabela 'secure_data'")

    return APIModel(api_key=data[0]["api_key"].strip().strip("'").strip('"'))

async def fetch_prompts() -> PromptModel:
    data = await fetch_from_supabase("prompts")
    
    if not data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado na tabela 'prompts'")
    
    return [
        PromptModel(
            prompt=d["prompt"],
            type=d.get("type"),
            category=d.get("category")
        )
        for d in data
    ]
