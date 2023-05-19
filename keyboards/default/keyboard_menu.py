from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Посмотреть результаты'),
        ],
        [
            KeyboardButton(text='Любимые команды'),
        ],
    ],
    resize_keyboard=True
)


rejection = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Без причины'),
        ],
    ],
    resize_keyboard=True
)
