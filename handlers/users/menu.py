from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp, datebase

from keyboards.default import keyboard_menu
from keyboards.inline import inline_kb_menu


@dp.message_handler(text='Посмотреть результаты')
async def menu(message: types.Message):
    await message.answer('Выберите нужную категорию',
                         reply_markup=inline_kb_menu.vidsporta_type)


@dp.callback_query_handler(text='back_to_cat')
async def menu(call: CallbackQuery):
    await call.message.edit_text('Выберите нужную категорию',
                                 reply_markup=inline_kb_menu.vidsporta_type)


@dp.callback_query_handler(text='solo_team')
async def solo_team(call: CallbackQuery):
    await call.message.edit_text('Выберите вид спорта',
                         reply_markup=inline_kb_menu.vidsporta_vid("False"))


@dp.callback_query_handler(text='team_teams')
async def team_teams(call: CallbackQuery):
    await call.message.edit_text('Выберите вид спорта',
                         reply_markup=inline_kb_menu.vidsporta_vid("True"))


@dp.callback_query_handler(text_startswith='backtovidsporta_')
async def menu(call: CallbackQuery):
    await call.message.edit_text('Выберите вид спорта',
                                 reply_markup=inline_kb_menu.vidsporta_vid(call.data.split('_')[1]))


@dp.callback_query_handler(text_startswith='teamsvidsporta_')
async def team_teams(call: CallbackQuery):
    vidsportaid = call.data.split('_')[1]
    if datebase.vidsporta_type(vidsportaid):
        text = 'Выберите название команды'
    else:
        text = 'Выберите ФИО игрока'
    await call.message.edit_text(text,
                         reply_markup=inline_kb_menu.team_by_vidsportaid(vidsportaid))




@dp.callback_query_handler(text='search_team')
async def search_team(call: CallbackQuery):
    pass



@dp.callback_query_handler(text_startswith='teamrange_')
async def team_teams(call: CallbackQuery):
    team_id = call.data.split('_')[1]
    type_ = datebase.vidsporta_type_by_team(team_id)
    team_name = datebase.teaminfo_by_id(team_id)[1]
    text = f'Список всех матчей "{team_name}" с баллами:\n\n'

    if type_:
        m1 = ''
    else:
        m1 = datebase.results_solo_byteam(team_id)

    if len(m1) > 0:
        c = 1
        for i in m1:
            text += f'{c}. {i[0]} - {i[1]} баллов\n'

        await call.message.answer(text)
    else:
        await call.message.answer(f"{'Команда' if type_ else 'Участник'} '{team_name}' ещё не участвовал(-а)")


@dp.callback_query_handler(text_startswith='teamstatus_')
async def team_teams(call: CallbackQuery):
    team_id = call.data.split('_')[1]
    final = datebase.final_results_byteam(team_id)
    type_ = datebase.vidsporta_type_by_team(team_id)
    team_name = datebase.teaminfo_by_id(team_id)[1]

    text = f"{'Команда' if type_ else 'Участник'} '{team_name}' "
    if bool(len(final)):
        m1 = datebase.final_results_byteam(team_id)
        text += f' занял(-а) {m1[0][1]} место!'
        await call.message.answer(text)
    else:
        text += f' ещё не занял(-а) призового места, возможно соревнования всё ещё продолжаются!'
        await call.message.answer(text)


@dp.message_handler(text='Любимые команды')
async def menu(message: types.Message):
    await message.answer("I am so sorry, заработает с обновлением")


@dp.message_handler()
async def menu(message: types.Message):
    await message.answer('*приветсвие*' + str(message.chat.id),
                         reply_markup=keyboard_menu.main)

