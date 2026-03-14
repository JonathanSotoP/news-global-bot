from transformers import pipeline
import re

print("Cargando modelo de traducción...")

translator = pipeline(
    "text-generation",
    model="Helsinki-NLP/opus-mt-en-es"
)

print("Modelo cargado")


def simple_summary(text):

    sentences = re.split(r'[.!?]', text)

    clean = []

    for s in sentences:
        s = s.strip()
        if len(s) > 40:
            clean.append(s)

    return ". ".join(clean[:2])


def translate(text):

    result = translator(text, max_new_tokens=120)

    output = result[0]["generated_text"]

    return output.strip()


def analyze_news(title, text):

    try:

        text = text[:1000]

        summary = simple_summary(text)

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