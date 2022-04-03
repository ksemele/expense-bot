from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Available commands: ",
            "/start - Launch bot.",
            "/help - Commands list, little help.",
            "/add - Add expense.",
            "/edit - Edit expense.",
            "/list - See my expenses.",
            "/settings - Configure bot.",
            "/test - Test command."
            )
    
    await message.answer("\n".join(text))
