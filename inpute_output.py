import re

from settings import MIN_LENHGTH, MAX_LENHGTH


def input_genre():
    """Валидация строки жанра."""
    genre_list = ['Drama', 'Comedy', 'Musical',
                  'Detective', 'Action', 'Horror']
    while True:
        genre = input(f'Введите название категории из списка {genre_list}: ')
        if genre in genre_list:
            return genre
        else:
            print(f'Название категории должно быть из списка {genre_list}')


def input_city():
    """Валидация строки город."""
    pattern = '^[A-Za-zА-Яа-яЁё\s\-]+$'
    while True:
        city = input('Введите город: ')
        if re.match(pattern, city):
            return city
        else:
            print('Ошибка: Название города содержит недопустимые символы.')


def input_length():
    """Валидация длинны рассказа."""
    while True:
        length = int(input('Введите длину рассказа в символах: '))
        if length < MIN_LENHGTH:
            print(f'Получиться слишком короткий рассказ, введи больше {MIN_LENHGTH}')
        elif length > MAX_LENHGTH:
            print(f'Слишком много символов, введи меньше {MAX_LENHGTH}')
        else:
            return length


def output(response):
    """Вывод в консоль."""
    print(f'Ответ получен от: {response[2]}, длительность запроса: {response[1]}, файл: {response[2]}_response.txt')


def save_in_file(response):
    """Сохранения данных в файл."""
    if response[2] == 'GigaChat':
        text = response[0]['choices'][0]['message']['content']
    else:
        text = response[0]["result"]["alternatives"][0]['message']['text']
    with open(f'{response[2]}_response.txt', 'w') as file:
        file.write(text)
