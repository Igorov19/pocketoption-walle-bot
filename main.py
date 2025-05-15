from aiogram import Bot, Dispatcher, types, executor
import os

bot = Bot(token=os.getenv("ТОКЕН"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Купити", "Продати")
    await message.answer("Обери дію:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ["Купити", "Продати"])
async def trade_handler(message: types.Message):
    if message.text == "Купити":
        await message.answer("Виконую купівлю...")
    else:
        await message.answer("Виконую продаж...")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
