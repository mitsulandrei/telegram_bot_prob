from aiogram import types
from loader import dp

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name},\nТвой id - {message.from_user.id}')