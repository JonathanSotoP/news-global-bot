from transformers import pipeline

print("Cargando modelo IA...")

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

print("Modelo cargado")


def analyze_news(title, text):

    try:

        text = text[:1500]

        prompt = f"""
Traduce el siguiente título al español y resume la noticia en español.

Título:
{title}

Contenido:
{text}

Responde en este formato:

TITULO:
(título en español)

RESUMEN:
(resumen claro de la noticia)
"""

        result = generator(
            prompt,
            max_new_tokens=150,
            do_sample=False
        )

        output = result[0]["generated_text"]

        message = f"""
🌍 NOTICIA GLOBAL IMPORTANTE

{output}
"""

        return message

    except Exception as e:

        print("Error IA:", e)

        return None