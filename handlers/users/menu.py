from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.keyboards_menu import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def open_menu(message: types.Message):
    await message.answer("Выбери меню", reply_markup=menu)