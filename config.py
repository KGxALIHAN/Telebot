from aiogram import Bot,Dispatcher
from dotenv import dotenv_values
from database.db import Database


token = dotenv_values('.env')['TOKEN']
bot=Bot(token=token)
dp = Dispatcher()
db = Database('database/db.sqlite3')


