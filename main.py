from datetime import datetime
import requests
import asyncio


from yandex_gpt import get_requests_yandex
from inpute import input_genre

from gigachat_gpt import get_promt_gigachat


key = 'Api-key AQVNyCfgUCawzeHHwKA1pjY2G0nXC-_N-mlQEP1e'


def get_city_location(city):
    api_key = 'ec4b6970-5c79-4ff8-a566-f8e1d899c61f'
    base_url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'geocode': city,
        'apikey': api_key,
        'format': 'json',
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        try:
            coords = (response.json()['response']['GeoObjectCollection']
                      ['featureMember'][0]['GeoObject']['Point']['pos']
                      )
            longitude, latitude = map(float, coords.split())
            return latitude, longitude
        except (KeyError, IndexError, ValueError):
            print('Город не найден или данные не доступны')
    else:
        print('Ошибка при получении координат')


def get_weather(city):
    api_key = '46f1cbbca65cad26389133ee943cd628'
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'

    latitude, longitude = get_city_location(city)
    # Формируем параметры запроса
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'cnt': 2,
        'units': 'metric',
        'lang': 'ru',
    }

    # Делаем запрос к API
    response = requests.get(base_url, params=params)
    data = response.json()
    # Получаем информацию о погоде на завтра
    temperature = data['list'][1]['main']['temp']
    weather_description = data['list'][1]['weather'][0]['description']
    return f'температура: {temperature}, {weather_description}'


def get_text_request(city, genre, length, weather):
    return f'Напиши сказку в жанре {genre} о погоде в городе {city}. Прогноз на завтра: {weather}. Длина сказки - {length} символов.'


async def get_request_to_model(model_name, message):
    if model_name == 'yandexGPT':
        start_time = datetime.now()
        response = get_requests_yandex(message)
        end_time = datetime.now()
        result = response.json()["result"]["alternatives"][0]['message']['text']
        duration = end_time - start_time
        return result, duration
    else:
        start_time = datetime.now()
        response = get_promt_gigachat(
            message
            ).json()['choices'][0]['message']['content']
        end_time = datetime.now()
        duration = end_time - start_time
        return response, duration
    

def save_in_file(text, name_model):
    with open(f'{name_model}_response.txt', 'w') as file:
        file.write(text[0])


async def main():
    city = input('Введите город: ')
    genre = input_genre()
    length = int(input('Введите длину рассказа в символах: '))
    weather = get_weather(city)
    message = get_text_request(city, genre, length, weather)
    yandexGPT = asyncio.create_task(get_request_to_model('yandexGPT', message))
    giga_chat = asyncio.create_task(get_request_to_model('Gigachat', message))
    yandex_response = await (yandexGPT)
    giga_chat_response = await (giga_chat)
    save_in_file(yandex_response, 'yandexGPT')
    save_in_file(giga_chat_response, 'gigachat')
    print(f'Название модели: yandexGPT, Длительность запроса: {yandex_response[1]}, файл: yandexGPT_response.txt')
    print(f'Название модели: giga_chat, Длительность запроса: {giga_chat_response[1]}, файл: gigachat_response.txt')

if __name__ == '__main__':
    asyncio.run(main())
