from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Launch bot."),
            types.BotCommand("help", "Commands list, little help."),
            types.BotCommand("add", "Add expense."),
            types.BotCommand("edit", "Edit expense."),
            types.BotCommand("list", "See my expenses."),
            types.BotCommand("settings", "Configure bot."),
            types.BotCommand("test", "Test command."),
            # types.BotCommand("settings3", "Configure bot."),
        ]
    )
