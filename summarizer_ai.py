import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {}

if HF_TOKEN:
    headers["Authorization"] = f"Bearer {HF_TOKEN}"


def summarize(text):

    payload = {
        "inputs": text[:2000],
        "parameters": {
            "max_length": 220,
            "min_length": 120,
            "do_sample": False
        }
    }

    try:

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=40
        )

        data = response.json()

        if isinstance(data, list) and "summary_text" in data[0]:
            return data[0]["summary_text"]

        if isinstance(data, dict) and "error" in data:
            print("HuggingFace error:", data["error"])

        return text[:600] + "..."

    except Exception as e:
        print("Error en summarize:", e)
        return text[:600] + "..."
