from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("ТОКЕН")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Купити", "Продати"]
    keyboard.add(*buttons)
    await message.answer("Привіт! Обери дію:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Купити")
async def buy_handler(message: types.Message):
    await message.reply("Купівля підтверджена.")

@dp.message_handler(lambda message: message.text == "Продати")
async def sell_handler(message: types.Message):
    await message.reply("Продаж підтверджений.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
