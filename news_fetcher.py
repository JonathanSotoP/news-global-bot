import feedparser
from sources import RSS_SOURCES

def fetch_news():
    news = []
    for url in RSS_SOURCES:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            news.append({
                "title": entry.get("title",""),
                "summary": entry.get("summary",""),
                "link": entry.get("link","")
            })
    return news