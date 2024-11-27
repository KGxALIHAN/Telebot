from aiogram import Bot,Dispatcher,types,Router,F
from aiogram.filters import Command

start_router= Router()

kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='review',callback_data = 'review' )]
])


@start_router.message(Command('start'))
async def start(message:types.Message):
    await message.answer(f'hello {message.from_user.first_name}',reply_markup=kb)

@start_router.callback_query(F.data == 'hi')
async def hi(call: types.CallbackQuery):
    await call.message.answer('HIIIIIIIIII')