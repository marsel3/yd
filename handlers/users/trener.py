from loader import dp, datebase
from keyboards.inline import inline_kb_menu
from aiogram.dispatcher import FSMContext
from aiogram import types
from states.state import RegistrationTrener
from aiogram.types import CallbackQuery



@dp.message_handler(text='/trener')
async def command_start(message: types.Message):
    if datebase.user_status(message.from_user.id) == 'trener':
        text, markup = inline_kb_menu.trener_menu(message.from_user.id)
        await message.answer(text, reply_markup=markup)

    else:
        await message.answer(f'У вас нет статуса "тренер", хотите оставить заявку?'
                             f'\nподготовьте, можете всегда отмена',
                             reply_markup=inline_kb_menu.start_be_trener)



@dp.callback_query_handler(text='start_be_trener')
async def start_be_trener(call: CallbackQuery):
    await RegistrationTrener.contact.set()

    if call.from_user.username == None:
        await call.message.answer('Введите ваш номер для связи', reply_markup=inline_kb_menu.back_menu)
    else:
        await call.message.answer('Введите ваше ФИО', reply_markup=inline_kb_menu.back_menu)
        state = dp.get_current().current_state()
        async with state.proxy() as data:
            data["contact"] = '@' + call.from_user.username
        await RegistrationTrener.next()


@dp.message_handler(state=RegistrationTrener.contact)
async def trener_fio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fio'] = message.text
    await message.answer('Введите ваше ФИО', reply_markup=inline_kb_menu.back_menu)
    await RegistrationTrener.next()

@dp.message_handler(state=RegistrationTrener.fio)
async def trener_fio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fio'] = message.text
    await message.answer(f'{message.text}, введите серию и номер паспорта в формате "1234 567890"',
                         reply_markup=inline_kb_menu.back_menu)
    await RegistrationTrener.next()


@dp.message_handler(state=RegistrationTrener.passport)
async def trener_passport(message: types.Message, state: FSMContext):
    passport = message.text
    if len(passport.split()) > 1 and passport.split()[0].isdigit() and passport.split()[1].isdigit():
        async with state.proxy() as data:
            data['passport'] = passport
            await message.answer(f'{message.text}, введите вашу тренерскую квалификацию',
                                 reply_markup=inline_kb_menu.back_menu)
            await RegistrationTrener.next()
    else:
        await message.answer(f'Паспортные данные не приняты!\n'
                             f'{message.text}, введите серию и номер паспорта в формате "1234 567890"',
                             reply_markup=inline_kb_menu.back_menu)
        await RegistrationTrener.passport.set()


@dp.message_handler(state=RegistrationTrener.kval)
async def trener_passport(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['kval'] = message.text
        oldTrener = datebase.trener_by_passport(data["passport"])
        text = ''
        if oldTrener:
            text += "Тренер с указзанным паспортом уже есть в базе!!!\n\n"

        text += f'{data["fio"]}:' \
                f'\nПаспорт: {data["passport"]}\nКвалификация: {data["kval"]}\n' \
                f'Телеграм ID: {message.from_user.id}\n\nДля связи: {data["contact"]}'

    await message.answer('Отлично! Заявка создана, наш менеджер свяжется с вами, в случае ошибки заполнения '
                         'анкеты вы получите соответствующее сообщение!')
    await dp.bot.send_message(chat_id='-600665752',
                              text=text,
                              reply_markup=inline_kb_menu.make_trener(message.from_user.id))
    await state.finish()



