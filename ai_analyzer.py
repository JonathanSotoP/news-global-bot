from transformers import pipeline

print("Cargando modelo IA...")

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

print("Modelo cargado")


def analyze_news(title, text):

    try:

        text = text[:1200]

        prompt = f"""
Traduce al español y resume la siguiente noticia.

Titulo: {title}

Contenido: {text}

Devuelve SOLO esto:

TITULO: traduccion del titulo
RESUMEN: resumen en español
"""

        result = generator(
            prompt,
            max_new_tokens=120,
            do_sample=False
        )

        output = result[0]["generated_text"].strip()

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

{output}
"""

        return message

    except Exception as e:

        print("Error IA:", e)
        return None