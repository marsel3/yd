from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ℹ️Главная страница'),
        ],
    ],
    resize_keyboard=True
)
