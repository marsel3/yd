from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from loader import dp, datebase
from states.state import *
from keyboards.default import keyboard_menu
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text='test1')
async def test1(call: CallbackQuery):
    await call.message.edit_text('C новой обновой заработает...')


@dp.callback_query_handler(text='back_menu')
async def back_menu(call: CallbackQuery):
    await call.answer('Вы вернулись в главное меню!')



@dp.callback_query_handler(text_startswith='setTrener_')
async def back_menu(call: CallbackQuery):
    t, user_id, bol = call.data.split('_')
    if bol == 'True':
        if datebase.trener_by_tg(user_id):
            datebase.set_status(user_id, 'trener')
            await dp.bot.send_message(chat_id=user_id,
                                      text='Поздравляю, администратор подтвердил ваш статус. '
                                           'Воспользуйтесь командой /trener')
            await call.message.edit_reply_markup()
            await dp.bot.send_message(chat_id=call.message.chat.id,
                                      text='Заявка успешно подтверждена!')
        else:
            await call.message.answer('Я не буду ломать БД! Сначала добавь тренера в БД, потом выдавай статус!!!')
    else:
        await call.message.edit_reply_markup()
        await call.message.answer('Напиши причину отказа: ', reply_markup=keyboard_menu.rejection)
        await RejectionTrener.user_id.set()
        state = dp.get_current().current_state()
        async with state.proxy() as data:
            data["user_id"] = user_id
        await RejectionTrener.next()


@dp.callback_query_handler(text_startswith='createTeam_')
async def back_menu(call: CallbackQuery):
    t, user_id, bol = call.data.split('_')
    if bol == 'True':
        trener_id = datebase.trener_info(user_id)[0]
        if datebase.team_by_trener(trener_id):
            await dp.bot.send_message(chat_id=user_id,
                                      text='Поздравляю, администратор подтвердил создание команды. '
                                           'Воспользуйтесь командой /trener для управления')
            await call.message.edit_reply_markup()
            await dp.bot.send_message(chat_id=call.message.chat.id,
                                      text='Заявка успешно подтверждена!')
        else:
            await call.message.answer('Я не буду ломать БД! Сначала добавь команду в БД и свяжи с тренером, потом выдавай статус!!!')
    else:
        await call.message.edit_reply_markup()
        await call.message.answer('Напиши причину отказа: ', reply_markup=keyboard_menu.rejection)
        await RejectionTrener.user_id.set()
        state = dp.get_current().current_state()
        async with state.proxy() as data:
            data["user_id"] = user_id
        await RejectionTrener.next()


@dp.callback_query_handler(text_startswith='sostavChange_')
async def back_menu(call: CallbackQuery):
    t, user_id, bol = call.data.split('_')
    if bol == 'True':
        await dp.bot.send_message(chat_id=user_id,
                                  text='Поздравляю, администратор подтвердил создание команды. '
                                       'Воспользуйтесь командой /trener для управления')
        await call.message.edit_reply_markup()
        await dp.bot.send_message(chat_id=call.message.chat.id,
                                  text='Заявка успешно подтверждена!')
    else:
        await call.message.edit_reply_markup()
        await call.message.answer('Напиши причину отказа: ', reply_markup=keyboard_menu.rejection)
        await RejectionTrener.user_id.set()
        state = dp.get_current().current_state()
        async with state.proxy() as data:
            data["user_id"] = user_id
        await RejectionTrener.next()


@dp.message_handler(state=RejectionTrener.rejection)
async def rejection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await dp.bot.send_message(chat_id=data["user_id"],
                                  text=f'Ваша заявка отклонена. Причина: "{message.text}"')
    await dp.bot.send_message(chat_id=message.chat.id,
                              text='Заявка отклонена успешно!', reply_markup=ReplyKeyboardRemove())
    await state.finish()
