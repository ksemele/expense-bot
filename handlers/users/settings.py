from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandSettings

from loader import dp


@dp.message_handler(CommandSettings())
async def bot_settings(message: types.Message):
    await message.answer(f"Settings being here...")
