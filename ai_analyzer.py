import requests
from bs4 import BeautifulSoup
import os

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}"
}


def clean_html(text):

    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def analyze_news(title, content):

    try:

        content = clean_html(content)
        content = content[:1200]

        prompt = f"""
Traduce al español y resume la siguiente noticia.

Titulo:
{title}

Contenido:
{content}

Responde SOLO así:

TITULO:
(titulo en español)

RESUMEN:
(resumen claro en español en 3 lineas)
"""

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 180
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        result = response.json()

        text = result[0]["generated_text"]

        return f"🌍 NOTICIA GLOBAL IMPORTANTE\n\n{text}"

    except Exception as e:

        print("Error IA:", e)
        return None