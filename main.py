import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)

# Клавіатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Купити"), KeyboardButton("Продати"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Вибери дію:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Купити")
async def buy(message: types.Message):
    await message.answer("Ти натиснув: Купити")

@dp.message_handler(lambda message: message.text == "Продати")
async def sell(message: types.Message):
    await message.answer("Ти натиснув: Продати")

if __name__ == "__main__":
    executor.start_polling(dp)
