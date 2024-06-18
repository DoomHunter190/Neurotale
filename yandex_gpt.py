import requests

yandex_indf = 'b1gddig4d67h2ikc7i3q'

yandex_indf_key = 'aje84vg509lgpngsfg50'

key = 'Api-key AQVNyCfgUCawzeHHwKA1pjY2G0nXC-_N-mlQEP1e'

url_yandex = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

key_giga='b2703af0-919d-4297-9466-2411639e96d5'

author_data ='N2U3NDAxM2YtMDEwOC00N2I2LTkyMjQtNjg1ZTNkNjljYjdjOmIyNzAzYWYwLTkxOWQtNDI5Ny05NDY2LTI0MTE2MzllOTZkNQ=='


def get_requests_yandex(meessage):
    prompt = {
        "modelUri": f"gpt://{yandex_indf}/yandexgpt/latest",
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
            'Authorization': key
        }

    response = requests.post(url=url_yandex, headers=headers, json=prompt)

    return response
