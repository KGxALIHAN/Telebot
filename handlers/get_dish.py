from aiogram import Bot,Dispatcher,types,Router,F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from config import db

get_dish_router= Router()



@get_dish_router.message(Command('get_dish'))
async def get(m:types.Message):
    data=db.fetch("""SELECT name,cost FROM dish ORDER BY cost""")
    for i in data:
        await m.answer(f'name:{i['name']}\ncost:{i['cost']}')
