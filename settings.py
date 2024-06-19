import os

from dotenv import load_dotenv

load_dotenv()

# Максимальное и минимальное кол-во символов.

MIN_LENHGTH = 300

MAX_LENHGTH = 2000

# API URLS

URL_REQUESTS_YANDEX = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'  # noqa

URL_TOKEN_GIGACHAT = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'

URL_REQUESTS_GIGACHAT = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"   # noqa

URL_REQUESTS_WEATHER = 'https://api.openweathermap.org/data/2.5/forecast'

URL_REQUESTS_CITY = 'https://geocode-maps.yandex.ru/1.x/'


# API KEYS

AUTH_TOKEN_GIGACHAT = os.getenv('AUTH_TOKEN_GIGACHAT')

API_KEY_CITY = os.getenv('API_KEY_CITY')

API_KEY_WEATHER = os.getenv('API_KEY_WEATHER')

KEY_API_YANDEX = os.getenv('KEY_API_YANDEX')

YANDEX_INDF = os.getenv('YANDEX_INDF')
