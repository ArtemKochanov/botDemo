import asyncio
import logging
import sys
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import command_start_handler, echo_handler, cmd_inline_url, cmd_random, reply_builder
from loader import mr, dp, bot, TOKEN

async def main() -> None:
    dp.message.register(command_start_handler)
    dp.message.register(echo_handler)
    dp.message.register(cmd_inline_url)
    dp.message.register(cmd_random)
    dp.message.register(reply_builder)
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
