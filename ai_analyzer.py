import requests
from config import HF_TOKEN

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_news(title, article):

    prompt = f"""
Analiza la siguiente noticia internacional.

1 Traduce el título al español
2 Resume la noticia en español (1000 caracteres)
3 Explica por qué es importante globalmente
4 Explica cómo podría impactar en Chile

Formato:

TITULO:
...

RESUMEN:
...

IMPACTO EN CHILE:
- ...
- ...

NOTICIA:
{title}

{article}
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 400
        }
    }

    try:

        r = requests.post(API_URL, headers=headers, json=payload, timeout=60)

        data = r.json()

        if isinstance(data, list):
            return data[0]["generated_text"]

        return None

    except:

        return None