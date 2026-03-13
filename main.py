from news_fetcher import fetch_news
from news_filter import is_relevant
from summarizer_ai import summarize
from telegram_sender import send_message
from impact_chile import analyze_impact

def run():

    news_list = fetch_news()

    sent = 0

    for news in news_list:

        if not is_relevant(news):
            continue

        title = news["title"]
        text = title + ". " + news["summary"]

        # resumen largo en español
        summary = summarize(
            f"""
Resume esta noticia en español en aproximadamente 1200-1500 caracteres.

Incluye:
- contexto global
- por qué es importante
- posibles consecuencias económicas o geopolíticas

Noticia:
{text}
"""
        )

        # análisis de impacto en Chile
        impacts = analyze_impact(text)

        impact_text = ""
        for i, imp in enumerate(impacts):
            impact_text += f"{i+1}. {imp}\n"

        message = f"""🌎 **NOTICIA GLOBAL RELEVANTE**

📰 **Titular**
{title}

📊 **Resumen**
{summary}

🇨🇱 **Impacto posible en Chile**
{impact_text}

🔗 **Fuente**
{news["link"]}
"""

        send_message(message)

        sent += 1

        # máximo 3 noticias por ejecución
        if sent >= 3:
            break


if __name__ == "__main__":
    run()
