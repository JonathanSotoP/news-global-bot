from transformers import pipeline
from bs4 import BeautifulSoup
import re

print("Cargando modelo IA...")

generator = pipeline(
    "text-generation",
    model="gpt2"
)

print("Modelo cargado")


def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def clean_ai_output(text):

    # eliminar el prompt si aparece
    text = text.replace("Traduce al español y resume la siguiente noticia.", "")
    text = text.replace("Titulo:", "TITULO:")
    text = text.replace("Contenido:", "")
    text = text.replace("Responde EXACTAMENTE en este formato:", "")

    # eliminar espacios repetidos
    text = re.sub(r"\n\s*\n", "\n\n", text)

    return text.strip()


def analyze_news(title, content):

    try:

        content = clean_html(content)
        content = content[:800]

        prompt = f"""
Traduce al español y resume esta noticia.

Titulo: {title}

Contenido: {content}

Formato de respuesta:

TITULO:
RESUMEN:
"""

        result = generator(
            prompt,
            max_length=220,
            do_sample=True,
            temperature=0.3
        )

        text = result[0]["generated_text"]

        text = clean_ai_output(text)

        return f"🌍 NOTICIA GLOBAL IMPORTANTE\n\n{text}"

    except Exception as e:

        print("Error IA:", e)
        return None