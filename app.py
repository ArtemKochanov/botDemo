import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram.client.default import DefaultBotProperties
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

@dp.message()
async def handle_message(message: types.Message):
    if message.sender_chat and message.sender_chat.type == "channel":
        photo = FSInputFile("image.jpg")

        await message.reply_photo(
            photo=photo,
            caption=RULES_TEXT
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())