import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(msg):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {

        "chat_id": CHAT_ID,
        "text": msg

    }

    requests.post(url, json=payload)