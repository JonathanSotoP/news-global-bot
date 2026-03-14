import requests
from bs4 import BeautifulSoup


def extract_article(url):

    try:

        r = requests.get(url, timeout=20)

        soup = BeautifulSoup(r.text, "lxml")

        paragraphs = soup.find_all("p")

        text = ""

        for p in paragraphs:
            text += p.get_text() + " "

        return text[:4000]

    except:

        return ""