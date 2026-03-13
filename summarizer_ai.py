import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {}

if HF_TOKEN:
    headers["Authorization"] = f"Bearer {HF_TOKEN}"


def summarize(text):

    prompt = f"""
Resume la siguiente noticia en español.

Requisitos:
- Entre 1000 y 1500 caracteres
- Explica el contexto global
- Explica por qué es relevante
- Explica posibles efectos económicos o políticos en Chile
- Usa español claro

Noticia:
{text}
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300,
            "min_length": 120
        }
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=40
        )

        data = response.json()

        # Caso normal
        if isinstance(data, list) and "summary_text" in data[0]:
            return data[0]["summary_text"]

        # Si HuggingFace devuelve error
        if isinstance(data, dict) and "error" in data:
            print("HuggingFace error:", data["error"])

        # fallback simple si falla la IA
        return text[:600] + "..."

    except Exception as e:
        print("Error en summarize:", e)
        return text[:600] + "..."
