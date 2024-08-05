from aiogram import F
from aiogram.filters import CommandStart
from aiogram import types
from aiogram import Router
from aiogram.types import Message
from loader import mr, dp
from aiogram.filters.command import Command

from aiogram.utils.markdown import hbold


@dp.message(Command("start"))
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f'Hello, {hbold(message.from_user.full_name)}!')

@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Error')
