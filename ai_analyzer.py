import requests
from config import HF_TOKEN

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_news(title, article):

    prompt = f"""
Traduce el titulo al español y analiza la noticia.

Entrega la respuesta en español con este formato:

TITULO:
(titulo en español)

RESUMEN:
(resumen claro de la noticia)

IMPACTO EN CHILE:
- impacto economico o politico
- impacto en cobre, comercio o dolar si aplica

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