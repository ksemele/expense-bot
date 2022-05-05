from aiogram import types
from loader import dp
import json


@dp.message_handler(commands="currencies")
async def get_currencies(message: types.Message):
    import requests
    import datetime
    url = 'https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/'
    date = datetime.date.today().isoformat()
    payload = {'currencies': ['USD', 'EUR'], 'date': date}
    r = requests.get(url, params=payload)
    print(r.text)
    usd = json.loads(r.text)
    for elem in usd:
        # print(elem['currencies'])
        for each in elem['currencies']:
            # print(each)
            # print(each['code'] + " " + each['rateFormated'])
            await message.answer(each['code'] + " " + each['rateFormated'])
    # print(r.status_code)
