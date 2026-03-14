import feedparser
from telegram_sender import send_message
from ai_analyzer import analyze_news


RSS_URL = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"


def get_news():

    feed = feedparser.parse(RSS_URL)

    return feed.entries[:10]


def main():

    print("Buscando noticias...")

    news = get_news()

    print("Noticias encontradas:", len(news))

    analyzed = []

    for item in news:

        title = item.title
        content = item.summary

        print("Analizando:", title)

        score, message = analyze_news(title, content)

        analyzed.append((score, message))

    analyzed.sort(reverse=True)

    top_news = analyzed[:3]

    for _, message in top_news:

        send_message(message)


if __name__ == "__main__":
    main()