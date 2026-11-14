import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

load_dotenv()

# 1. ВКЛЮЧАЕМ ЖУРНАЛ СОБЫТИЙ (Логирование)
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("TOKEN")

# 2. СОЗДАЕМ ТЕЛО И МОЗГ
bot = Bot(token = BOT_TOKEN) # Твое тело (выполняет приказы)
dp = Dispatcher() # Твой мозг (принимает решения)

# 3. СТАВИМ ЛОВУШКУ (Хэндлер)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Запуск систем...")
    await message.answer(f"Привет! {message.from_user.first_name}! Бот готов к работе!")

@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Это  бот помощник. Я пока ничего не умею, но скоро научусь!")
    
# dp.message(Command("start"))  // Во-первых, нет @
# async def cmd_start(message: Message):  // Во-вторых, просто Message нельзя передавать
#     message.answer("Привет!")  // В-третьих, нет await


@dp.message(F.sticker)
async def all_message(message: types.Message):
    await message.answer_sticker(f'{message.sticker.file_id}')

@dp.message(F.text)
async def all_message(message: types.Message):
    await message.answer(f'{message.text} 🦜')
    await message.answer(f"Привет {message.from_user.first_name}! В твоем сообщении {len(message.text)} символов!")
    # await message.reply(f'{message.text} 🦜')

# 4. ЗАПУСК ДВИГАТЕЛЯ
async def main():
    await dp.start_polling(bot)

# 5. КРАСНАЯ КНОПКА СТАРТА
if __name__ == "__main__":
    asyncio.run(main())