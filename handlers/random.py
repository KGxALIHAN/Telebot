from aiogram import Bot,Dispatcher,types,Router
from aiogram.filters import Command
from random import choice

random_router= Router()
names = ('dfs','dsfs','sdfs')

@random_router.message(Command('random'))
async def random(message:types.Message):
     await message.answer(f'{choice(names)}')

