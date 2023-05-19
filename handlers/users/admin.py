from filters import IsAdmin
from aiogram import types

from loader import dp, datebase
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery



@dp.message_handler(IsAdmin(), text='/admin')
async def admin(messsage: types.Message):
    await messsage.answer(f'Здравствуйте, {messsage.from_user.full_name},  вы попали в админ панель!'
                          f' http://127.0.0.1:8000/admin/')

