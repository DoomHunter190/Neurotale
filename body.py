
yandex_indf = 'b1gddig4d67h2ikc7i3q'

yandex_indf_key = 'aje84vg509lgpngsfg50'

key = 'Api-key AQVNyCfgUCawzeHHwKA1pjY2G0nXC-_N-mlQEP1e'


key_giga='b2703af0-919d-4297-9466-2411639e96d5'

author_data ='N2U3NDAxM2YtMDEwOC00N2I2LTkyMjQtNjg1ZTNkNjljYjdjOmIyNzAzYWYwLTkxOWQtNDI5Ny05NDY2LTI0MTE2MzllOTZkNQ=='

def get_yandex_body(text):
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
                "text": text,
            }
        ]
    }

    

    return prompt


def get_gigachat_body(text):
    pass
