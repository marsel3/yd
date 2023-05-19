from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationTrener(StatesGroup):
    contact = State()
    fio = State()
    passport = State()
    kval = State()


class RejectionTrener(StatesGroup):
    user_id = State()
    rejection = State()