from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api import db_sqlite3, db_postgres
from data import config


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)


dp = Dispatcher(bot, storage=MemoryStorage())
#datebase = db_sqlite3.DataBase("db/users.db")
datebase = db_postgres.DataBase()