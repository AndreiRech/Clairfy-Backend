from fastapi import FastAPI

from app.routers import secrets

app = FastAPI()

def init(app: FastAPI) -> None:
    """
    Inicializa as rotas da aplicação
    """
    app.include_router(secrets.router)
    
init(app)