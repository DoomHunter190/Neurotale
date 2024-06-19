import json
import uuid

import requests
import urllib3

from settings import (AUTH_TOKEN_GIGACHAT, URL_REQUESTS_GIGACHAT,
                      URL_TOKEN_GIGACHAT)


def get_token(auth_token):
    """Токен для авторизации в GigaChat."""
    rq_uid = str(uuid.uuid4())
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth_token}'
    }
    payload = {
        'scope': 'GIGACHAT_API_PERS'
    }
    try:
        response = requests.post(url=URL_TOKEN_GIGACHAT,
                                 headers=headers,
                                 data=payload,
                                 verify=False
                                 )
        return response
    except requests.RequestException as error:
        return error


def get_requests_gigachat(message):
    """Запроса к GigaChatGPT."""
    giga_token = get_token(AUTH_TOKEN_GIGACHAT).json()['access_token']
    payload = json.dumps({
        'model': 'GigaChat',
        'messages': [
            {
                'role': 'user',
                'content': message

            }
        ],
        'temperature': 1,
        'top_p': 0.1,
        'n': 1,
        'stream': False,
        'max_tokens': 2000,
        'repetition_penalty': 1,
        'update_interval': 0

    })

    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {giga_token}'
        }
    try:
        response = requests.request('POST',
                                    url=URL_REQUESTS_GIGACHAT,
                                    headers=headers,
                                    data=payload,
                                    verify=False)
        return response
    except requests.RequestException as error:
        print(f'Ошибка {error}')
        return -1


urllib3.disable_warnings()
