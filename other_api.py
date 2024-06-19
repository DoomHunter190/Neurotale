import requests

from http import HTTPStatus
from settings import (API_KEY_CITY, API_KEY_WEATHER, URL_REQUESTS_CITY,
                      URL_REQUESTS_WEATHER)


def get_city_location(city):
    """Геолокации города."""
    params = {
        'geocode': city,
        'apikey': API_KEY_CITY,
        'format': 'json',
    }
    try:
        response = requests.get(URL_REQUESTS_CITY, params=params)
    except Exception as error:
        raise Exception(f'Ошибка при запросе к API геолокации {error}.')
    if response.status_code != HTTPStatus.OK:
        print('Ошибка при получении координат')
    else:
        coords = (
            response.json()['response']['GeoObjectCollection']
            ['featureMember'][0]['GeoObject']['Point']['pos']
                )
        longitude, latitude = map(float, coords.split())
        return latitude, longitude


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
    try:
        response = requests.get(URL_REQUESTS_WEATHER, params=params)
    except Exception as error:
        raise Exception(f'Ошибка при запросе к API погоды {error}.')
    if response.status_code != HTTPStatus.OK:
        print('Ошибка при получении погоды')
    else:
        data = response.json()
        temperature = data['list'][1]['main']['temp']
        weather_description = data['list'][1]['weather'][0]['description']
        return f'температура: {temperature}, {weather_description}'
