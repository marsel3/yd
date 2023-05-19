from aiogram import types



async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('trener', 'Тренер'),
        #types.BotCommand('player', 'Участник соревнований'),
        types.BotCommand('admin',  'Админ панель'),
    ])