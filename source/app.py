from loader import *


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


@dp.message(Command("currencies"))
async def get_currencies(message: types.Message):
    url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/"
    date = datetime.date.today().isoformat()
    payload = {"currencies": ["USD", "EUR"], "date": date}
    r = requests.get(url, params=payload)
    # print(r.text)
    usd = json.loads(r.text)
    for elem in usd:
        # print(elem['currencies'])
        for each in elem["currencies"]:
            # print(each)
            # print(each['code'] + " " + each['rateFormated'])
            await message.answer(each["code"] + " " + each["rateFormated"])
    # print(r.status_code)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
