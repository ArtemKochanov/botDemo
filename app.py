import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

RULES_TEXT = """📌 Добро пожаловать в чат
Правила чата:
🚫 Спам — <b>бан</b>  
🚫 Доксинг — <b>бан</b>  
🚫 Оскорбления — <b>бан</b>  

💀 Оскорбление администрации — расстрел, потом <b>бан</b>
Всем удачи...
"""

BAD_WORDS = [
    "хуй",
    "залупа",
    "пизда",
    "гандон",
]

warnings = {}

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💖 Поддержать автора",
                url="https://www.tinkoff.ru/rm/r_qEkoNlpkfl.hcwycHOMII/1fRzk69171"
            )
        ]
    ]
)

@dp.message()
async def handle_message(message: types.Message):

    # ПОСТЫ КАНАЛА
    if message.sender_chat and message.sender_chat.type == "channel":

        photo = FSInputFile("image.jpg")

        await message.reply_photo(
            photo=photo,
            caption=RULES_TEXT,
            reply_markup=keyboard
        )

        return

    # МОДЕРАЦИЯ
    if not message.text:
        return

    text = message.text.lower()

    for bad_word in BAD_WORDS:
        if bad_word in text:

            user_id = message.from_user.id

            warnings[user_id] = warnings.get(user_id, 0) + 1

            count = warnings[user_id]

            await message.reply(
                f"⚠️ {message.from_user.full_name}, предупреждение ({count}/3)"
            )

            break

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())