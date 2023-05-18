from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    test = State()
    FIO = State()
    phone = State()
    email = State()

