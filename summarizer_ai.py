import requests
from config import HF_TOKEN

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {}
if HF_TOKEN:
    headers["Authorization"] = f"Bearer {HF_TOKEN}"

def summarize(text):

    payload = {
        "inputs": text[:2000],
        "parameters": {"max_length": 200, "min_length": 80}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        data = response.json()

        if isinstance(data, list) and "summary_text" in data[0]:
            return data[0]["summary_text"]
    except:
        pass

    return text[:500]