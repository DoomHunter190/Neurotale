## Описание:
Neurotale - мини-приложение для написания нейроскази о погоде в городе на завтра с помощью GigaChatGPT и YandexGPT. Достаточно задать название города, длину, жанр, в котором вы хотите написать нейросказку и приложение автоматически получит информацию о погоде на завтра для указанного города, затем сгенерирует увлекательную и оригинальную нейросказку в указанном жанре и заданной длины с использованием мощных нейронных моделей GigaChatGPT и YandexGPT. Результат работы приложения будет сохранен в файле, чтобы пользователь мог сохранить и поделиться своей уникальной историей о завтрашней погоде в выбранном городе.

## Технологии:
* Python 3.11
* Python-dotenv 1.0.1
* Requests 2.32.3

## Установка
1. Клонировать проект из репозитория (ssh):

    ```git clone git@github.com:DoomHunter190/Neurotale.git```
  
2. Создайте вертуальное окружение:
 
    ```python -3.11 -m venv venv```

3. Установите зависимости:

    ```pip install -r requirements.txt```

4. Создайте файл ***.env*** в корневой папке и заполнить его данными по примеру ***.env.example***
    ```
    AUTH_TOKEN_GIGACHAT= 'Токен авторизации' https://developers.sber.ru/portal/products/gigachat-api
    
    API_KEY_CITY= 'JavaScript API и HTTP Геокодер' https://yandex.ru/maps-api/
    
    API_KEY_WEATHER= '5 Day / 3 Hour Forecast' https://openweathermap.org/api
    
    KEY_API_YANDEX= 'Ваш секретный ключ' https://yandex.cloud/ru/services/yandexgpt
    
    YANDEX_INDF= 'Индификатор каталога'https://yandex.cloud/ru/services/yandexgpt
    ```

   P.S Для проверки тестового задания:
    ```
    AUTH_TOKEN_GIGACHAT='N2U3NDAxM2YtMDEwOC00N2I2LTkyMjQtNjg1ZTNkNjljYjdjOjRhNThkM2IzLTI3MzQtNDA1ZC1hNTFmLWU1ZDAxYTc4YzYyYw=='
    
    API_KEY_CITY='ec4b6970-5c79-4ff8-a566-f8e1d899c61f'
    
    API_KEY_WEATHER='46f1cbbca65cad26389133ee943cd628'
    
    KEY_API_YANDEX='Api-key AQVNyCfgUCawzeHHwKA1pjY2G0nXC-_N-mlQEP1e'
    
    YANDEX_INDF='b1gddig4d67h2ikc7i3q'
    ```


### Запуск
Запустить файл main.py:

```python main.py  ```



Автор | Почта
------------- | -------------
[Doomhunter190](https://github.com/DoomHunter190) | <small>[maximportnov9999@gmail.com](maximportnov9999@gmail.com)
