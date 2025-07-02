from fastapi import HTTPException, status
import os

def check_token(x_token: str):
    """
    Verifica se o token de acesso enviado no cabeçalho está correto.
    Lança uma exceção 401 se for inválido.
    """
    if x_token != os.getenv("ACCESS_TOKEN"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")