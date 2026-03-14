from news_fetcher import get_news
from ai_analyzer import analyze_news
from telegram_sender import send_message

print("Buscando noticias...")

news = get_news()

print("Noticias encontradas:", len(news))

for article in news:

    print("Analizando:", article["title"])

    analysis = analyze_news(
        article["title"],
        article["summary"]
    )

    if analysis:

        message = analysis + f"\n🔗 Fuente:\n{article['link']}"

        send_message(message)

        print("Mensaje enviado")