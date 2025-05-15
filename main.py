import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Завантаження змінних із .env / Railway
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Налаштування бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда старт
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer("Бот працює! Готовий до команд.")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
