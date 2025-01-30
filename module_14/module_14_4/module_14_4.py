from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = "7657515087:AAG_ARGejcu5_heVJwzbS89wL5b-j91WkDI"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
bt1 = KeyboardButton(text="Рассчитать")
bt2 = KeyboardButton(text="Информация")
bt3 = KeyboardButton(text="Купить")
kb.add(bt1, bt2)
kb.add(bt3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
bt3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
bt4 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
kb2.add(bt3, bt4)

kb_buy = InlineKeyboardMarkup(resize_keyboard=True)
bt_buy1 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
bt_buy2 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
bt_buy3 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
bt_buy4 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
kb_buy.row(bt_buy1, bt_buy2, bt_buy3, bt_buy4)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(f"files/{product[0]}.png", "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_buy)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

@dp.message_handler(text="Информация")
async def info(message):
    await message.answer("Тут будет информация")

@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb2)

@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.message.answer("для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()

class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text="calories")
async def set_gender(call):
    await call.message.answer("Введите свой пол цифрой:\n1. Женщина\n2. Мужчина")
    await call.answer()
    await UserState.gender.set()

@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text)
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if data["gender"] == "1":
        formula_woman = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 161
        await message.answer(f'Ваша женская норма калорий в сутки равна: {formula_woman} ккал.')
        await message.answer('Рассчитано по упрощенному варианту формулы Миффлина-Сан Жеора.')
    elif data["gender"] == "2":
        formula_man = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5
        await message.answer(f'Ваша мужская норма калорий в сутки равна {formula_man} ккал.')
        await message.answer('Рассчитано по упрощенному варианту формулы Миффлина-Сан Жеора.')
    elif int(data["gender"]) != "1" or "2":
        await message.answer("Вы неверно ввели цифру, чтобы указать свой пол!\nПожалуйста, попробуйте еще раз! 😊")
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

def main():
    executor.start_polling(dp, skip_updates=True)
if __name__ == "__main__":
    main()
