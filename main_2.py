import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
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

# Создание инлайн-кнопок с URL-ссылками
links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Новости", url="https://climaterealism.com/2025/01/from-idealism-to-realism/"),
        InlineKeyboardButton(text="Музыка", url="https://soundcloud.com/search?q=boiler%20room&query_urn=soundcloud%3Asearch-autocomplete%3Afdf19c9fcf3d4f49a5c32245ecf5ed06")
    ],
    [
        InlineKeyboardButton(text="Видео", url="https://w140.zona.plus/tvseries/sorvigolova-2015")
    ]
])

# Обработчик команды /links
@dp.message(Command("links"))
async def send_links(message: Message):
    await message.answer(
        "Выберите одну из ссылок:",
        reply_markup=links_keyboard
    )

# Основной цикл
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
