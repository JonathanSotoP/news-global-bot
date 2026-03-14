from news_fetcher import fetch_news
from relevance_filter import is_relevant
from article_extractor import extract_article
from ai_analyzer import analyze_news
from telegram_sender import send_message


def run():

    news_list = fetch_news()

    sent = 0

    for news in news_list:

        if not is_relevant(news):
            continue

        article = extract_article(news["link"])

        if len(article) < 500:
            continue

        analysis = analyze_news(news["title"], article)

        if not analysis:
            continue

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

{analysis}

Fuente:
{news["link"]}
"""

        send_message(message)

        sent += 1

        if sent >= 3:
            break


if __name__ == "__main__":
    run()