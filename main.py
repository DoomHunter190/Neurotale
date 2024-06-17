import datetime, timedelta
import requests

def get_city_location(city):
    api_key = 'YOUR_GOOGLE_API_KEY'
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': city,
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        print(f'Геолокация города {city}: Широта - {latitude}, Долгота - {longitude}')
    else:
        print('Геолокация не найдена')
    return latitude, longitude

def get_weather(latitude, longitude):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = 'https://api.openweathermap.org/data/2.5/onecall'

    # Получаем текущую дату
    today = datetime.now()

    # Вычисляем дату на следующий день
    tomorrow = today + timedelta(days=1)

    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'exclude': 'current,minutely,hourly',  # Исключаем текущую, минутную и часовую погоду
        'units': 'metric'  # Возможные значения: 'metric', 'imperial', 'standard'
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        forecast = data['daily'][1]  # Прогноз на завтра
        weather = forecast['weather'][0]['description']
        
        print(f'Прогноз погоды на завтра:')
        print(f'Погода: {weather}')
    else:
        print('Ошибка при получении прогноза погоды')
    return weather


def create_prompt(city, genre, length, weather):
    prompt = (f'Напишите рассказ в жанре: {genre}, о погоде: {weather} в городе: {city} завтра.
              История не должна превышать {length} символов.')
    return prompt


def get_request_to_model(model_name, promt):
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
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
    genre = input_genre()
    length = int(input('Введите длину рассказа в символах: '))
    location = get_city_location(city)
    longitude = location['latitude']
    latitude = location['longitude']
    weather = get_weather()

    prompt = create_prompt(city, genre, length, weather)
    yandex_gpt_duration = get_request_to_model("YandexGPT", prompt)
    gigachat_duration = get_request_to_model("GigaChat", prompt)
    with open("yandexgpt_response.txt", "w") as file:
        file.write("YandexGPT response")

    with open("gigachat_response.txt", "w") as file:
        file.write("GigaChat response")
    
    print("YandexGPT:", yandex_gpt_duration, "seconds", "yandexgpt_response.txt")
    print("GigaChat:", gigachat_duration, "seconds", "gigachat_response.txt")

if __name__ == '__main__':
    main()
