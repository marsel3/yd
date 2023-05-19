from aiogram import types
from loader import dp, datebase


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    if not datebase.user_exists(message.from_user.id):
        datebase.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name, 'user')

    await message.answer(f'Привет {message.from_user.full_name}!')



