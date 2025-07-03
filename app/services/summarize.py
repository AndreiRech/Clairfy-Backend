import json
import os
import aiohttp
from fastapi import HTTPException, UploadFile
from app.models.responses import HealthResponse
from app.services.secrets import fetch_api_key, fetch_prompts
from dotenv import load_dotenv

load_dotenv()

async def transcribe_and_summarize(audio: UploadFile, type: str) -> str:
    """"
    Busca chave e Prompt -> Transcreve -> Resume
    """

    api_key = await fetch_api_key()
    prompts = await fetch_prompts()

    transcribed_text = await transcribe_audio(audio, api_key)

    doctor_prompts = next((p.prompt for p in prompts if p.type == type and p.category == "doctor"), None)
    patient_prompts = next((p.prompt for p in prompts if p.type == type and p.category == "patient"), None)

    if not doctor_prompts or not patient_prompts:
        raise HTTPException(status_code=404, detail="Prompts não encontrados para o tipo especificado.")
    
    doctor_response = await summarize_text(transcribed_text, doctor_prompts, api_key)
    patient_response = await summarize_text(transcribed_text, patient_prompts, api_key)

    if not doctor_response or not patient_response:
        raise HTTPException(status_code=500, detail="Erro ao resumir o texto transcrito.")
    
    try:
        doctor_json = json.loads(doctor_response)
        patient_json = json.loads(patient_response)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Erro ao decodificar a resposta JSON do resumo.")

    return HealthResponse(
        transcription=transcribed_text,
        summary=doctor_json.get("summary", ""),
        didctarized=doctor_json.get("didctarized", ""),
        keyWords=doctor_json.get("keyWords", ""),
        actionPoints=patient_json.get("actionPoints", "")
    )

async def transcribe_audio(audio: UploadFile, api_key: str) -> str:
    """
    Envia o áudio para a API da OpenAI e retorna o texto transcrito.
    """

    data = aiohttp.FormData()
    data.add_field("file", await audio.read(), filename=audio.filename, content_type=audio.content_type)
    data.add_field("model", "whisper-1")

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(os.getenv("OPENAI_TRANSCRIBE_URL"), data=data, headers=headers) as resp:
            if resp.status != 200:
                raise HTTPException(status_code=resp.status, detail="Erro na transcrição do áudio")
            response = await resp.json()
            return response.get("text")
        
async def summarize_text(text: str, prompt: str, api_key: str) -> str:
    """
    Envia um texto para o ChatGPT e retorna a resposta resumida.
    """

    body = {
        "model": "gpt-4.1-mini-2025-04-14",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        "temperature": 0.1
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(os.getenv("OPENAI_SUMMARIZE_URL"), json=body, headers=headers) as resp:
            if resp.status != 200:
                raise HTTPException(status_code=resp.status, detail="Erro na sumarização do texto")
            response = await resp.json()
            return response["choices"][0]["message"]["content"]

