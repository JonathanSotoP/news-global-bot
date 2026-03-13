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

        text = news["title"] + ". " + news["summary"]

        summary = summarize(text)

        impacts = analyze_impact(text)

        impact_text = ""
        for i,imp in enumerate(impacts):
            impact_text += f"{i+1}. {imp}\n"

        message = f"""🌎 NOTICIA GLOBAL

{summary}

Impacto posible en Chile:
{impact_text}

Fuente:
{news["link"]}
"""

        send_message(message)

        sent += 1

        if sent >= 3:
            break

if __name__ == "__main__":
    run()