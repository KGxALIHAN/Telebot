from aiogram import F, Router, types
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from config import db


admin_dish_router = Router()

admin_dish_router.message.filter(
    F.from_user.id == 6573322342
)

class Dish(StatesGroup):
    name = State()
    cost = State()


@admin_dish_router.message(Command("add_dish"), default_state)
async def create_dish(message: types.Message, state: FSMContext):
    await state.set_state(Dish.name)
    await message.answer("name of dish:")

@admin_dish_router.message(Dish.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Dish.cost)
    await message.answer("what is the price:")

@admin_dish_router.message(Dish.cost)
async def process_author(message: types.Message, state: FSMContext):
    await state.update_data(cost=message.text)
    data = await state.get_data()
    db.execute("""INSERT INTO dish VALUES (?,?,?)""",(None,data['name'],data['cost']))
    await message.answer("ok ok , dish is added")
    await state.clear()
