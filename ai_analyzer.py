from transformers import pipeline
from bs4 import BeautifulSoup
import re

print("Cargando modelo IA...")

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

print("Modelo cargado")


def clean_text(text):

    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def analyze_news(title, text):

    try:

        text = clean_text(text)

        text = text[:1200]

        prompt = f"""
Traduce al español y resume la siguiente noticia.

Titulo:
{title}

Contenido:
{text}

Responde EXACTAMENTE en este formato:

TITULO:
(titulo traducido al español)

RESUMEN:
(resumen claro en español en 3-4 lineas)
"""

        result = generator(
            prompt,
            max_length=250,
            do_sample=False
        )

        response = result[0]["generated_text"]

        return f"🌍 NOTICIA GLOBAL IMPORTANTE\n\n{response}"

    except Exception as e:

        print("Error IA:", e)

        return None