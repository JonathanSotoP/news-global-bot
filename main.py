from news_fetcher import fetch_news
from relevance_filter import is_relevant
from article_extractor import extract_article
from ai_analyzer import analyze_news
from telegram_sender import send_message


def run():

    print("Buscando noticias...")

    news_list = fetch_news()

    print("Noticias encontradas:", len(news_list))

    sent = 0

    for news in news_list:

        print("Evaluando:", news["title"])

        if not is_relevant(news):
            print("No es relevante")
            continue

        article = extract_article(news["link"])

        print("Tamaño articulo:", len(article))

        if len(article) < 500:
            print("Artículo demasiado corto")
            continue

        analysis = analyze_news(news["title"], article)

        if not analysis:
            print("IA no respondió")
            continue

        message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

{analysis}

Fuente:
{news["link"]}
"""

        send_message(message)

        print("Mensaje enviado")

        sent += 1

        if sent >= 3:
            break


if __name__ == "__main__":
    run()