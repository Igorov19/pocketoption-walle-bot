import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# Завантаження змінних з .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

# Налаштування логів
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Клавіатура з кнопками
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Купити"), KeyboardButton("Продати"))

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Обери дію:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Купити")
async def buy_handler(message: types.Message):
    await message.answer("Угода 'Купити' виконана.")

@dp.message_handler(lambda message: message.text == "Продати")
async def sell_handler(message: types.Message):
    await message.answer("Угода 'Продати' виконана.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
