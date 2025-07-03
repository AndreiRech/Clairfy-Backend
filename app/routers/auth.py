from fastapi import APIRouter
from app.models.auth import TokenModel

from app.services.auth import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token", response_model=TokenModel, status_code=200)
async def generate_token():
    """
    Gera um token JWT para ser usado pela aplicação iOS.
    Esse token pode ser armazenado no Secrets.swift.
    """

    response = create_token()

    return response
