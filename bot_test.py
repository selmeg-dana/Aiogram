import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

# 1. ВКЛЮЧАЕМ ЖУРНАЛ СОБЫТИЙ (Логирование)
logging.basicConfig(level=logging.INFO)

# 2. СОЗДАЕМ ТЕЛО И МОЗГ
bot = Bot(token="8961675119:AAGBhew00kZY8OYV5R2z0qcR31Oh-KWJMMQ") # Твое тело (выполняет приказы)
dp = Dispatcher()                    # Твой мозг (принимает решения)

# 3. СТАВИМ ЛОВУШКУ (Хэндлер)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой первый бот! 🚀")
    await message.answer(f"Привет! {message.from_user.first_name}! Я проснулся!🚀")

@dp.message(F.text)
async def all_message(message: types.Message):
    await message.answer(f'{message.text} 🦜')

# 4. ЗАПУСК ДВИГАТЕЛЯ
async def main():
    await dp.start_polling(bot)

# 5. КРАСНАЯ КНОПКА СТАРТА
if __name__ == "__main__":
    asyncio.run(main())