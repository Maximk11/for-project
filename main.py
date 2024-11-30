import requests

def get_weather(city_name: str, state_name: str, api_key_value: str) -> None:
    """
    Узнаем погоду в городе (и области, если нужно).

    Указываем город, область (если есть) и API-ключ от OpenWeather.
    Функция подтягивает данные с сервера и выводит температуру, влажность,
    скорость ветра и описание текущей погоды.

    Параметры:
    city_name (str): Название города (например, "Москва").
                     Если не указано, будет использована только область или регион.
    state_name (str): Название области или региона (например, "Московская область").
                      Если не указано, будет использован только город.
    api_key_value (str): Твой API-ключ для OpenWeather (его нужно заранее получить).

    Если данные введены некорректно, сервер вернёт ошибку с кодом.
    """
    if state_name:
        location = f'{city_name},{state_name},RU'
    else:
        location = f'{city_name},RU'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key_value}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f'Погода в городе {city_name} ({state_name if state_name else "область не указана"}):')
        print(f'Температура: {temp}°C')
        print(f'Влажность: {humidity}%')
        print(f'Ветер: {wind_speed} м/с')
        print(f'Описание погоды: {weather}')
    else:
        print(f'Ошибка! Код ошибки: {response.status_code}. Проверьте правильность введенных данных.')

if __name__ == "__main__":
    api_key_value = ''
    city_name = input('Введите город: ')
    state_name = input('Введите область (если нет — оставьте пустым): ')
    get_weather(city_name, state_name, api_key_value)