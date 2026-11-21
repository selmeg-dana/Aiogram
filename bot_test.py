import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

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

@dp.message(Command("my_card"))
async def all_photo(message: types.Message):
    photo_file = FSInputFile("C:\Aiogram\Photo\winter.jpg")

    await message.answer_photo(
            photo = photo_file,
            caption = f"Зима крутая аватарка! \nВот твои имя и ID: {message.from_user.first_name}, {message.from_user.id}"
                              )

@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("Это  бот помощник. Я пока ничего не умею, но скоро научусь!")
    
@dp.message(Command("cat"))
async def all_photo(message: types.Message):
    photo_file = FSInputFile("C:\Aiogram\Photo\cat.jpg")

    await message.answer_photo(
            photo = photo_file,
            caption = "Милый котик"
                              )
    
# dp.message(Command("start"))  // Во-первых, нет @
# async def cmd_start(message: Message):  // Во-вторых, просто Message нельзя передавать
#     message.answer("Привет!")  // В-третьих, нет await



@dp.message(F.sticker)
async def all_stickers(message: types.Message):
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