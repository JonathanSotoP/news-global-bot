from transformers import pipeline

print("Cargando modelos IA...")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-es"
)

print("Modelos cargados")


def analyze_news(title, text):

    try:

        text = text[:2000]

        summary = summarizer(
            text,
            max_length=120,
            min_length=50,
            do_sample=False
        )[0]["summary_text"]

        title_es = translator(title)[0]["translation_text"]

        summary_es = translator(summary)[0]["translation_text"]

        message = f"""
🌍 NOTICIA GLOBAL IMPORTANTE

📰 TITULO:
{title_es}

📄 RESUMEN:
{summary_es}
"""

        return message

    except Exception as e:

        print("Error IA:", e)

        return None