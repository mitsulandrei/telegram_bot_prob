from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню погоды'),
            KeyboardButton(text='Меню курcа валют'),
        ]
    ],
    resize_keyboard=True
    )
