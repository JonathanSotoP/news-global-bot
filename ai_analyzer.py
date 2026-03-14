from transformers import pipeline

print("Cargando modelo IA...")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("Modelo cargado")


def analyze_news(title, text):

    try:

        text = text[:800]

        prompt = f"""
Traduce al español y resume la siguiente noticia.

Titulo: {title}

Contenido: {text}

Respuesta en este formato:

TITULO:
RESUMEN:
"""

        result = generator(
            prompt,
            max_new_tokens=120,
            do_sample=False
        )

        output = result[0]["generated_text"]

        # eliminar prompt
        output = output.replace(prompt, "").strip()

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

{output}
"""

        return message

    except Exception as e:

        print("Error IA:", e)
        return None