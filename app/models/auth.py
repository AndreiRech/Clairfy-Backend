from pydantic import BaseModel

class TokenModel(BaseModel):
    token: str
    