import requests
from bs4 import BeautifulSoup
import os
import time

API_URL = "https://router.huggingface.co/hf-inference/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    "Content-Type": "application/json"
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

Responde SOLO en este formato:

TITULO:
(titulo en español)

RESUMEN:
(resumen claro en español en 3 lineas)
"""

        payload = {
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            print("Error IA:", response.text)
            return None

        result = response.json()

        text = result["choices"][0]["message"]["content"]

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

{text}
"""

        return message

    except Exception as e:

        print("Error IA:", e)
        return None