from contextlib import suppress
from random import randint

from aiogram import F, types, Router, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message
from loader import mr, dp
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.filters.command import Command
from aiogram.utils.markdown import hbold


@dp.message(Command("start"))
async def command_start_handler(message: types.Message):
    await message.answer(f'Hello, {hbold(message.from_user.full_name)}!')
    kb = [
        [types.KeyboardButton(text='/inline_url')],
        [types.KeyboardButton(text='/start')],
        [types.KeyboardButton(text='Robot, but they said me - i`m not a robot')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='What you may write in input text, i think this is miracle!'
    )
    await message.answer("Who are you?", reply_markup=keyboard)

@dp.message(Command("inline"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()

    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com/ArtemKochanov/botDemo/tree/master")
        )
    builder.row(types.InlineKeyboardButton(
        text="Telegram", url="https://t.me/artemandreich")
        )

    user_id = 574641346
    chat_info = await bot.get_chat(message.chat.id)
    if not chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
            text="Someone user", url=f"tg://user?id={user_id}")
            )

    await message.answer("Choose url", reply_markup=builder.as_markup())

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="tap me",
        callback_data="random_value"
    ))
    await message.answer("Tap on button for random number",
                         reply_markup=builder.as_markup())

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    with suppress(TelegramBadRequest):
        await callback.message.answer(str(randint(1, 10)))
        await callback.answer()

@dp.message(Command("reply_builder"))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(types.KeyboardButton(text=str(i)))
        builder.adjust(4)
    await message.answer(
        "Choose a number", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Error')

