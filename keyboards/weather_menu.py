from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

weather_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Написать город'),
            KeyboardButton(text='Ссылка на Gismeteo')
        ],
    ],
    resize_keyboard=True
)
