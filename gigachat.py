import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload='scope=GIGACHAT_API_PERS'

client_id='b2703af0-919d-4297-9466-2411639e96d5'

udi = '1b373685-49f6-42e1-a7be-176020c60420'

author_data ='N2U3NDAxM2YtMDEwOC00N2I2LTkyMjQtNjg1ZTNkNjljYjdjOmIyNzAzYWYwLTkxOWQtNDI5Ny05NDY2LTI0MTE2MzllOTZkNQ=='

def get_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': udi,
        'Authorization': f'Basic {author_data}'
    }
    response = requests.post(url, headers=headers, data=payload)
    result = response.json()
    return result


print(get_token())
