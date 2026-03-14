from transformers import pipeline
from bs4 import BeautifulSoup
import re

print("Cargando modelo de traducción...")

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-es"
)

print("Modelo cargado")


def clean_text(text):

    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def summarize(text):

    sentences = re.split(r'[.!?]', text)

    clean = []

    for s in sentences:
        s = s.strip()

        if len(s) > 40:
            clean.append(s)

    return ". ".join(clean[:2])


def translate(text):

    result = translator(text, max_length=200)

    return result[0]["translation_text"]


def analyze_news(title, text):

    try:

        text = clean_text(text)

        text = text[:1000]

        summary = summarize(text)

        title_es = translate(title)

        summary_es = translate(summary)

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

📰 TITULO:
{title_es}

📄 RESUMEN:
{summary_es}
"""

        return message

    except Exception as e:

        print("Error IA:", e)

        return None