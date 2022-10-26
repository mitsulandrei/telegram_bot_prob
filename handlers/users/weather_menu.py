import datetime
import requests
from aiogram import types
from loader import dp
from data.config import WEATHER_TOKEN
from keyboards.weather_menu import weather_menu
from keyboards.inline_kb import inline_kb
from pprint import pprint



@dp.message_handler(text='Меню погоды')
async def show_w_menu(message: types.Message):
    await message.answer('Напиши город или перейди по ссылке', reply_markup=weather_menu)

@dp.message_handler()
async def get_weather(message: types.Message):
    get_smile_code = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
}
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

        await message.answer(f'*** Прогноз погоды ***\n'
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
        await message.answer('Ведите правильное название города')


@dp.message_handler(text='Ссылка на Gismeteo')
async def get_w_url(message: types.Message):
    await message.answer('Нажми на ссылку',reply_markup=inline_kb)

