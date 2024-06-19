import requests

from settings import (API_KEY_CITY, URL_REQUESTS_CITY,
                      API_KEY_WEATHER, URL_REQUESTS_WEATHER)


def get_city_location(city):
    """Геолокации города."""
    params = {
        'geocode': city,
        'apikey': API_KEY_CITY,
        'format': 'json',
    }

    response = requests.get(URL_REQUESTS_CITY, params=params)

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
    """Погоды на завтра."""
    latitude, longitude = get_city_location(city)
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': API_KEY_WEATHER,
        'cnt': 2,
        'units': 'metric',
        'lang': 'ru',
    }
    response = requests.get(URL_REQUESTS_WEATHER, params=params)
    data = response.json()
    temperature = data['list'][1]['main']['temp']
    weather_description = data['list'][1]['weather'][0]['description']
    return f'температура: {temperature}, {weather_description}'
