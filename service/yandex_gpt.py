import requests
from http import HTTPStatus

from settings import KEY_API_YANDEX, URL_REQUESTS_YANDEX, YANDEX_INDF


def get_requests_yandex(meessage):
    """Запрос к YandexGPT."""
    prompt = {
        'modelUri': f'gpt://{YANDEX_INDF}/yandexgpt/latest',
        'completionOptions': {
            'stream': False,
            'temperature': 0.6,
            'maxTokens': '2000'
        },
        'messages': [
            {
                'role': 'system',
                'text': 'Ты — писатель.'
            },
            {
                'role': 'user',
                'text': meessage,
            }
        ]
    }

    headers = {
            'Content-Type': 'application/json',
            'Authorization': KEY_API_YANDEX
        }
    try:
        response = requests.post(url=URL_REQUESTS_YANDEX,
                                 headers=headers,
                                 json=prompt
                                 )
    except Exception as error:
        raise Exception(f'Ошибка при запросе к YandexGPT {error}.')
    if response.status_code != HTTPStatus.OK:
        print('Ошибка при получении ответа от YandexGPT')
    else:
        return response
