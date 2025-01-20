import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
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

# Создание клавиатуры с кнопкой "Показать больше"
def get_initial_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])

# Создание клавиатуры с кнопками "Опция 1" и "Опция 2"
def get_options_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ])

# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def send_dynamic_keyboard(message: Message):
    await message.answer(
        "Выберите действие:",
        reply_markup=get_initial_keyboard()
    )

# Обработчик callback для "Показать больше"
@dp.callback_query(lambda cq: cq.data == "show_more")
async def show_more_options(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите одну из опций:",
        reply_markup=get_options_keyboard()
    )

# Обработчик callback для "Опция 1" и "Опция 2"
@dp.callback_query(lambda cq: cq.data in ["option_1", "option_2"])
async def handle_option_selection(callback: CallbackQuery):
    option_text = "Опция 1" if callback.data == "option_1" else "Опция 2"
    await callback.message.answer(f"Вы выбрали: {option_text}")
    await callback.answer()  # Закрытие уведомления

# Основной цикл
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
