from bs4 import BeautifulSoup
import re
from heapq import nlargest


important_keywords = [
    "war","attack","military","crisis","economy","oil","inflation",
    "china","russia","usa","nato","israel","iran","ukraine",
    "earthquake","flood","disaster","explosion","terror",
    "market","stocks","global","energy"
]


def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def summarize(text, n=3):

    sentences = re.split(r'(?<=[.!?]) +', text)

    if len(sentences) <= n:
        return " ".join(sentences)

    word_frequencies = {}

    for word in re.findall(r'\w+', text.lower()):
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    maximum = max(word_frequencies.values())

    for word in word_frequencies:
        word_frequencies[word] /= maximum

    sentence_scores = {}

    for sent in sentences:
        for word in re.findall(r'\w+', sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    summary_sentences = nlargest(n, sentence_scores, key=sentence_scores.get)

    return " ".join(summary_sentences)


def importance_score(title, content):

    text = (title + " " + content).lower()

    score = 0

    for keyword in important_keywords:
        if keyword in text:
            score += 5

    score += len(content) / 500

    return score


def analyze_news(title, content):

    content = clean_html(content)

    score = importance_score(title, content)

    summary = summarize(content, 3)

    message = f"""🌍 NOTICIA GLOBAL IMPORTANTE

TITULO:
{title}

RESUMEN:
{summary}
"""

    return score, message