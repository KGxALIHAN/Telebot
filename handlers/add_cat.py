from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from config import db


admin_dish_router = Router()

admin_dish_router.message.filter(
    F.from_user.id == 6698434567
)

class Dish(StatesGroup):
    name = State()
    dish_id = State()


@admin_dish_router.message(Command("add_dish"), default_state)
async def create_dish(message: types.Message, state: FSMContext):
    await state.set_state(Dish.name)
    await message.answer("name of cat:")

@admin_dish_router.message(Dish.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    db.execute("""INSERT INTO dish_cat VALUES(?,?)""",(None,data['name']))
    await state.clear()