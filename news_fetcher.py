import feedparser

RSS_FEEDS = [

"https://feeds.bbci.co.uk/news/world/rss.xml",
"https://rss.cnn.com/rss/edition_world.rss",
"https://www.aljazeera.com/xml/rss/all.xml",
"https://www.reuters.com/world/rss",
"https://feeds.npr.org/1004/rss.xml"

]


def fetch_news():

    news = []

    for feed_url in RSS_FEEDS:

        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:5]:

            news.append({
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link
            })

    return news