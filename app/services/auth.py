from datetime import datetime, timedelta
import os

from fastapi import HTTPException, Header
from fastapi import security
from fastapi.params import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError

from app.models.auth import TokenModel
from dotenv import load_dotenv

security = HTTPBearer()

load_dotenv()

def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Valida o token JWT passado no header.
    """
    
    try:
        payload = jwt.decode(credentials.credentials, os.getenv("ACCESS_TOKEN"), algorithms=[os.getenv("ALGORITHM")])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token JWT inválido ou expirado.")
    
def create_token() -> TokenModel:
    payload = {
        "client": "clarify-ios",
        "exp": datetime.now() + timedelta(days=365)
    }
    token = jwt.encode(payload, os.getenv("ACCESS_TOKEN"), algorithm=os.getenv("ALGORITHM"))

    return TokenModel(token=token)