import datetime
import requests
from aiogram import types
from loader import dp
from data.config import WEATHER_TOKEN
from keyboards.weather_menu import weather_menu
from keyboards.inline_kb import inline_kb
from weather.main_tg_bot import get_weather
from pprint import pprint



@dp.message_handler(text='Меню погоды')
async def show_w_menu(message: types.Message):
    await message.answer('Напиши город или перейди по ссылке', reply_markup=weather_menu)

@dp.message_handler(text='Написать город:')
async def weather(message: types.Message):
    await message.answer('В каком городе искать погоду?')



@dp.message_handler(text='Ссылка на Gismeteo')
async def get_w_url(message: types.Message):
    await message.answer('Нажми на ссылку',reply_markup=inline_kb)

