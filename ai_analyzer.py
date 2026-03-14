import requests
from config import HF_TOKEN

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_news(title, article):

    prompt = f"""
Analiza la siguiente noticia internacional.

1. Traduce el título al español.
2. Resume la noticia en español (500 a 900 caracteres).
3. Explica por qué es importante globalmente.
4. Analiza cómo podría impactar en Chile.

Responde EXACTAMENTE en este formato:

TITULO:
(titulo en español)

RESUMEN:
(resumen)

IMPACTO EN CHILE:
- impacto 1
- impacto 2

NOTICIA:
Titulo: {title}

Contenido:
{article[:2000]}
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300
        }
    }

    try:

        r = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        data = r.json()

        print("Respuesta IA:", data)

        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]

        return None

    except Exception as e:

        print("Error IA:", e)

        return None