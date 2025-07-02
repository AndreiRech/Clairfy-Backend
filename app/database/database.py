import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

async def fetch_from_supabase(table: str):
    async with httpx.AsyncClient() as client:
        url = f"{SUPABASE_URL}/rest/v1/{table}?select=*"
        response = await client.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise Exception(f"Erro ao buscar {table}: {response.text}")
        return response.json()
