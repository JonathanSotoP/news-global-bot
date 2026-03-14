import requests
from bs4 import BeautifulSoup


def extract_article(url):

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers, timeout=20)

        soup = BeautifulSoup(r.text, "lxml")

        paragraphs = soup.find_all("p")

        text = ""

        for p in paragraphs:
            t = p.get_text().strip()

            if len(t) > 40:
                text += t + " "

        return text[:5000]

    except Exception as e:

        print("Error extrayendo artículo:", e)

        return ""