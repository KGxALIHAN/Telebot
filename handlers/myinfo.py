from aiogram import Bot,Dispatcher,types,Router
from aiogram.filters import Command

my_info_router= Router()

@my_info_router.message(Command('myinfo'))
async def my_info(message:types.Message):
    await message.answer(f'ur data:\nid:{message.from_user.id}\nfirst_name:{message.from_user.first_name}\nusername:{message.from_user.username}')

