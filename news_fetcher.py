import feedparser

RSS_FEEDS = [

"https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
"https://feeds.bbci.co.uk/news/world/rss.xml",
"https://www.aljazeera.com/xml/rss/all.xml",
"https://rss.cnn.com/rss/edition_world.rss"

]

KEYWORDS = [

"war","military","conflict","china","russia","iran",
"nato","economy","oil","sanctions","global",
"us","attack","missile","crisis"

]


def is_relevant(title):

    title = title.lower()

    for k in KEYWORDS:
        if k in title:
            return True

    return False


def get_news():

    news = []

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries:

            if is_relevant(entry.title):

                news.append({

                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.summary

                })

    return news[:5]