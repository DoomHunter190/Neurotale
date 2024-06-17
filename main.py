from datetime import datetime, timedelta
import requests

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
            print(f'Координаты города {city}: Широта - {latitude}, Долгота - {longitude}')
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
    return temperature, weather_description


def create_prompt(city, genre, length, weather):
    prompt = (f'Напишите рассказ в жанре: {genre}, о погоде: {weather} в городе: {city}. История не должна превышать {length} символов.')
    return prompt


def get_request_to_model(model_name, promt):
    start_time = datetime.now()
    end_time = datetime.now()
    duration = end_time - start_time
    return duration.total_seconds()


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
    #genre = input_genre()
    #length = int(input('Введите длину рассказа в символах: '))
    latitude, longitude = get_city_location(city)
    print(latitude)
    print(longitude)
    weather = get_weather(latitude, longitude)
    print('Погода: ', weather)

    #prompt = create_prompt(city, genre, length, weather)
    #yandex_gpt_duration = get_request_to_model("YandexGPT", prompt)
    #gigachat_duration = get_request_to_model("GigaChat", prompt)
    #with open("yandexgpt_response.txt", "w") as file:
    #    file.write("YandexGPT response")

    #with open("gigachat_response.txt", "w") as file:
    #    file.write("GigaChat response")
    
    #print("YandexGPT:", yandex_gpt_duration, "seconds", "yandexgpt_response.txt")
    #print("GigaChat:", gigachat_duration, "seconds", "gigachat_response.txt")

if __name__ == '__main__':
    main()
