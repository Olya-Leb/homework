from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7657515087:AAHJnq6KyawlN0mGQ8cz_tcEaMbmOxwkyl8" #123:abc
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message):
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_massages(message):
    print("Введите команду /start, чтобы начать общение.")

def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()