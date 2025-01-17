from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = " "
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text="Calories")
async def set_gender(message):
    await message.answer("Введите свой пол цифрой:\n"
                         "1. Женщина\n"
                         "2. Мужчина")
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
    if int(data["gender"]) == 1:
        formula_woman = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 161
        await message.answer(f'Ваша женская норма калорий в сутки равна: {formula_woman} ккал.')
        await message.answer('Рассчитано по упрощенному варианту формулы Миффлина-Сан Жеора.')
    elif int(data["gender"]) == 2:
        formula_man = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5
        await message.answer(f'Ваша мужская норма калорий в сутки равна {formula_man} ккал.')
        await message.answer('Рассчитано по упрощенному варианту формулы Миффлина-Сан Жеора.')
    elif int(data["gender"]) != 1 or 2:
        await message.answer("Вы неверно ввели цифру, чтобы указать свой пол!\nПожалуйста, попробуйте еще раз! 😊")
    await state.finish()


def main():
    executor.start_polling(dp, skip_updates=True)
if __name__ == "__main__":
    main()