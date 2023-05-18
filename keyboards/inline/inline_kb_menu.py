
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [InlineKeyboardButton(text='Запустить калькулятор', callback_data='start_process')
                                 ],

                                [InlineKeyboardButton(text='👤 Профиль', callback_data='profile'),
                                 InlineKeyboardButton(text='🆘 Тех. Поддержка', callback_data='help')
                                 ]
                            ])

