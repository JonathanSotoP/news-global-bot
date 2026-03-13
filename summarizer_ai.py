import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def summarize(text):

    prompt = f"""
Resume la siguiente noticia en español.

Requisitos:
- Máximo 1500 caracteres
- Explica claramente el contexto global
- Explica el posible impacto económico o político en Chile
- Usa lenguaje claro en español

Noticia:
{text}
"""

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    return result[0]["summary_text"]
