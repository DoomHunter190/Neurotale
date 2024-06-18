import requests

YANDEX_INDF = 'b1gddig4d67h2ikc7i3q'

# yandex_indf_key = 'aje84vg509lgpngsfg50'

KEY = 'Api-key AQVNyCfgUCawzeHHwKA1pjY2G0nXC-_N-mlQEP1e'

URL = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'


def get_requests_yandex(meessage):
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
            'Authorization': KEY
        }

    response = requests.post(url=URL, headers=headers, json=prompt)

    return response
