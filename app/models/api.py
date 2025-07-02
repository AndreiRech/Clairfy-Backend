from pydantic import BaseModel

class APIModel(BaseModel):
    api_key: str
    