from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Ссылка на сайт: ', url='https://www.gismeteo.md/')
                                    ]
                                 ]
)