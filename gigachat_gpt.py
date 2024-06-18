import requests
import uuid
import json
import urllib3

AUTH_TOKEN ='N2U3NDAxM2YtMDEwOC00N2I2LTkyMjQtNjg1ZTNkNjljYjdjOjRhNThkM2IzLTI3MzQtNDA1ZC1hNTFmLWU1ZDAxYTc4YzYyYw=='


def get_token(auth_token):
    rq_uid = str(uuid.uuid4())
    url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
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
        response = requests.post(url, headers=headers, data=payload,
                                 verify=False)
        return response
    except requests.RequestException as error:
        return error


def get_promt_gigachat(message):
    giga_token = get_token(AUTH_TOKEN).json()['access_token']
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
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
        response = requests.request('POST', url, headers=headers, data=payload,
                                    verify=False)
        return response
    except requests.RequestException as error:
        print(f'Ошибка {error}')
        return -1


urllib3.disable_warnings()
