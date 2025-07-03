from fastapi import FastAPI
from fastapi.security import HTTPBearer

from app.routers import secrets, auth, summarize

app = FastAPI()

def init(app: FastAPI) -> None:
    """
    Inicializa as rotas da aplicação
    """
    app.include_router(secrets.router)
    app.include_router(auth.router)
    app.include_router(summarize.router)
    
init(app)