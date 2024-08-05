from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
mr = Router()
dp = Dispatcher()

