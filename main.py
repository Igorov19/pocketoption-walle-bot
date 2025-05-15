from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("ТОКЕН"))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Купити"), types.KeyboardButton("Продати"))
    await message.answer("Бот активний! Обери дію:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Купити")
async def buy_handler(message: types.Message):
    await message.answer("Команда 'Купити' прийнята!")

@dp.message_handler(lambda message: message.text == "Продати")
async def sell_handler(message: types.Message):
    await message.answer("Команда 'Продати' прийнята!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
