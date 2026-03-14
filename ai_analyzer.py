import requests
from bs4 import BeautifulSoup
import os

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

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

        text = f"{title}. {content}"

        payload = {
            "inputs": text,
            "parameters": {
                "max_length": 130,
                "min_length": 40
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            print("Error IA:", response.text)
            return None

        result = response.json()

        summary = result[0]["summary_text"]

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

TITULO:
{title}

RESUMEN:
{summary}
"""

        return message

    except Exception as e:
        print("Error IA:", e)
        return None