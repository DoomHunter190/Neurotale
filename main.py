from datetime import datetime, timedelta
import requests

from body import get_yandex_body

url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'


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
    data = response.json()

    if response.status_code == 200:
        try:
            coords = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            longitude, latitude = map(float, coords.split())
            return latitude, longitude
        except (KeyError, IndexError, ValueError):
            print('Город не найден или данные не доступны')
    else:
        print('Ошибка при получении координат')


def get_weather(latitude, longitude):
    api_key = '46f1cbbca65cad26389133ee943cd628'
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'

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


def get_request_to_model(model_name, url, prompt):
    if model_name == 'yandexGPT':
        start_time = datetime.now()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': key
        }
        response = requests.post(url, headers=headers, json=prompt)
        result = response.json()
        end_time = datetime.now()
        result = result["result"]["alternatives"][0]['message']['text']
        duration = end_time - start_time
    return result, duration


def input_genre():
    genre_list = ['Drama', 'Comedy', 'Musical',
                  'Detective', 'Action', 'Horror']
    while True:
        genre = input('Введите название категории: ')
        if genre in genre_list:
            return genre
        else:
            print(f'Название категории должно быть из списка {genre_list}')


def main():
    city = input('Введите город: ')
    genre = input_genre()
    length = int(input('Введите длину рассказа в символах: '))
    latitude, longitude = get_city_location(city)
    weather = get_weather(latitude, longitude)
    prompt = get_yandex_body(get_text_request(city, genre, length, weather))
    yandexGPT = get_request_to_model('yandexGPT', url, prompt)

    #yandex_gpt_duration = get_request_to_model("YandexGPT", prompt)
    #gigachat_duration = get_request_to_model("GigaChat", prompt)
    with open("yandexgpt_response.txt", "w") as file:
        file.write(yandexGPT[0]) # доработать формат записи, убрать время

    print(f'Название модели: yandexGPT, Длительность запроса: {yandexGPT[1]}, файл: yandexgpt_response.txt')

    #with open("gigachat_response.txt", "w") as file:
    #    file.write("GigaChat response")
    
    #print("YandexGPT:", yandex_gpt_duration, "seconds", "yandexgpt_response.txt")
    #print("GigaChat:", gigachat_duration, "seconds", "gigachat_response.txt")

if __name__ == '__main__':
    main()
