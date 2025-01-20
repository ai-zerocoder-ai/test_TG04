import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

# Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Проверка токена
if not TOKEN:
    raise ValueError("Token is not set in the .env file")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание клавиатуры с reply-кнопками
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выберите действие:",
        reply_markup=main_keyboard
    )

# Обработчик кнопки "Привет"
@dp.message(lambda msg: msg.text == "Привет")
async def greet_user(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f"Привет, {user_name}!")

# Обработчик кнопки "Пока"
@dp.message(lambda msg: msg.text == "Пока")
async def say_goodbye(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f"До свидания, {user_name}!")

# Основной цикл
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
