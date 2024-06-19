import requests

from settings import YANDEX_INDF, KEY_API_YANDEX, URL_REQUESTS_YANDEX


def get_requests_yandex(meessage):
    """Запрос к YandexGPT."""
    prompt = {
        "modelUri": f"gpt://{YANDEX_INDF}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты — писатель."
            },
            {
                "role": "user",
                "text": meessage,
            }
        ]
    }

    headers = {
            'Content-Type': 'application/json',
            'Authorization': KEY_API_YANDEX
        }

    response = requests.post(url=URL_REQUESTS_YANDEX,
                             headers=headers,
                             json=prompt)

    return response
