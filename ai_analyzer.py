import requests
from bs4 import BeautifulSoup
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"

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
        content = content[:1000]

        prompt = f"""
Traduce al español y resume esta noticia.

Titulo:
{title}

Contenido:
{content}

Responde EXACTAMENTE así:

TITULO:
(titulo en español)

RESUMEN:
(resumen en 3 lineas)
"""

        payload = {
            "model": "mistralai/Mistral-7B-Instruct-v0.2",
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