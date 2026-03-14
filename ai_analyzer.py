import requests
from bs4 import BeautifulSoup
import os
import time

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    "Content-Type": "application/json"
}


def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def analyze_news(title, content):

    try:

        # limpiar HTML
        content = clean_html(content)

        # limitar tamaño para la IA
        content = content[:1200]

        prompt = f"""
Traduce al español y resume la siguiente noticia.

Titulo:
{title}

Contenido:
{content}

Responde SOLO en este formato:

TITULO:
(titulo traducido al español)

RESUMEN:
(resumen claro en español en 3-4 lineas)
"""

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 200
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        # si la respuesta no es válida
        if response.status_code != 200:
            print("Error IA:", response.text)
            return None

        result = response.json()

        # si el modelo está cargando
        if isinstance(result, dict) and "estimated_time" in result:

            print("Modelo cargando, esperando...")
            time.sleep(result["estimated_time"])

            response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code != 200:
                print("Error IA:", response.text)
                return None

            result = response.json()

        # si la API devuelve error
        if isinstance(result, dict) and "error" in result:
            print("Error IA:", result["error"])
            return None

        text = result[0]["generated_text"]

        return f"🌍 NOTICIA GLOBAL IMPORTANTE\n\n{text}"

    except Exception as e:

        print("Error IA:", e)
        return None