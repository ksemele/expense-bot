from aiogram import types
from loader import dp


@dp.message_handler(commands="add")
async def bot_add(message: types.Message):
    await message.answer(f"This is ADD command, {message.from_user.username}!")

    # @dp.message_handler(state=None)  # todo сделать стейты. сейчас это хэндлит все сообщения в любых состояниях!
    # async def bot_add_parse_message(message: types.Message):
    #     words = message.text.split()
    #     # Uncomment to see debug in console
    #     # print('Split message:')
    #     # i = 0
    #     # for each in words:
    #     #     print('[' + str(i) + ']: ' + '[' + each + ']')
    #     #     i += 1
    #     # print('[end]')
    #
    #     if len(words) == 2:
    #         await message.answer('[added] ' + words[0] + ' ' + words[1])
    #     else:
    #         await message.answer("can't parse. wrong arguments!")
