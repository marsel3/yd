from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp, datebase
from states.state import *
from keyboards.default import keyboard_menu
from keyboards.inline import inline_kb_menu
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(text_startswith='teamplayer_')
async def team_teams(call: CallbackQuery):
    team_id = call.data.split('_')[1]
    text, markup = inline_kb_menu.teamsolo_info(team_id)
    await call.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(text_startswith='teamchang_')
async def team_teams(call: CallbackQuery):
    team_id = call.data.split('_')[1]
    m1 = datebase.sporstmen_by_team(team_id)
    text = 'Текущий состав:\n\n'
    if len(m1) > 0:
        for i in m1:
            text += f'"{i[1]}" - {i[2]} лет'
    await call.message.answer(text, reply_markup=inline_kb_menu.edit_sostav)



@dp.callback_query_handler(text='edit_sostav')
async def team_teams(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('Введите новые свдения о сотаве в формате:'
                              '\n1. ФИО_игроока - возраст\n2. ФИО_игроока - возраст')
    await ChangeSostav.msg.set()

@dp.message_handler(state=ChangeSostav.msg)
async def trener_fio(message: types.Message, state: FSMContext):
    m1 = datebase.trener_info(message.from_user.id)
    text = f'Тренер "{m1[2]}" - паспорт({m1[3]})\n\nОставила(-а) заявку на изменения в составе:\n' + message.text
    await message.answer('Отлично! Заявка создана, наш менеджер свяжется с вами, в случае ошибки заполнения '
                         'анкеты вы получите соответствующее сообщение!')
    await dp.bot.send_message(chat_id='-600665752',
                              text=text,
                              reply_markup=inline_kb_menu.team_create(message.from_user.id))
    await state.finish()


