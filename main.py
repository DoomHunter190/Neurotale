import asyncio
from datetime import datetime

from service.gigachat_gpt import get_requests_gigachat
from service.inpute_output import (input_city, input_genre, input_length,
                                   output, save_in_file)
from service.other_api import get_weather
from service.yandex_gpt import get_requests_yandex


def get_text_request(city, genre, length):
    """Формирования сообщения запроса."""
    weather = get_weather(city)
    return (f'Напиши сказку в жанре {genre} о погоде в городе {city}. '
            f'Прогноз на завтра: {weather}. '
            f'Длина сказки не больше {length} символов.')


async def get_request_to_model(model_name, message):
    """Отправка запроса к моделям."""
    start_time = datetime.now()
    if model_name == 'YandexGPT':
        response = get_requests_yandex(message).json()
    else:
        response = get_requests_gigachat(message).json()
    end_time = datetime.now()
    duration = end_time - start_time
    return [response, duration, model_name]


async def main():
    print('Привет! Это Neurotale, давай напишем нейросказку!')
    city = input_city()
    genre = input_genre()
    length = input_length()
    message = get_text_request(city, genre, length)

    yandexGPT = asyncio.create_task(get_request_to_model('YandexGPT', message))
    giga_chat = asyncio.create_task(get_request_to_model('GigaChat', message))

    done, _ = await asyncio.wait([yandexGPT, giga_chat])

    for task in done:
        response = task.result()
        save_in_file(response)
        output(response)

if __name__ == '__main__':
    asyncio.run(main())
