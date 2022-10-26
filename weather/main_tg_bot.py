import requests
import datetime
from pprint import pprint
from data.config import WEATHER_TOKEN
from aiogram import types
from weather.smile_code import get_smile_code


async def get_weather(message: types.Message):

    try:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={WEATHER_TOKEN}&units=metric')
        data = res.json()
        pprint(data)

        city_name = data["name"]
        time_now = datetime.datetime.now().strftime('%H.%M')
        w_description = data["weather"][0]["main"]
        if w_description in get_smile_code:
            wd = get_smile_code[w_description]
        else:
            wd = 'Посмотри в окно'
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H.%M.%S')
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H.%M.%S')
        length_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f'*** Прогноз погоды ***\n'
              f'Город: {city_name}\n'
              f'Время: {time_now}\n'
              f'Температура: {cur_temp}°C. {wd}\n'
              f'Скорость ветра: {wind} м/с.\n'
              f'Влажность: {humidity}%.\n'
              f'Атмосферное давление: {pressure}\n'
              f'Время рассвета: {sunrise}\n'
              f'Время заката: {sunset}\n'
              f'Длительность дня: {length_day}\n'
              f'*** Хорошего дня ***')

    except:
        await message.reply('Ведите правильное название города')
