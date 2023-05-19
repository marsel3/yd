from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp

from keyboards.default import keyboard_menu
from keyboards.inline import inline_kb_menu



@dp.callback_query_handler(text_startswith='teamplayer_')
async def team_teams(call: CallbackQuery):
    team_id = call.data.split('_')[1]
    text, markup = inline_kb_menu.team_info(team_id)
    await call.message.edit_text(text, reply_markup=markup)





