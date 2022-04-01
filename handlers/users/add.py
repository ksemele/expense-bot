from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


@dp.message_handler(commands="add")
async def bot_add(message: types.Message):
    await message.answer(f"This is ADD command, {message.from_user.username}!")
