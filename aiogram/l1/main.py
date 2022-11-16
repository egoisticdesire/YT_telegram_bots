import os
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher, types, executor

load_dotenv(find_dotenv('.tokens'))
TOKEN = os.getenv('aiogramEgo_bot')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


# Задача: дублировать сообщение пользователя в том случае, если оно состоит из двух и более слов.
# Приводить к верхнему регистру
@dp.message_handler()
async def echo_upper(msg: types.Message):
    if ' ' in msg.text:
        await msg.answer(text=msg.text.upper())


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )
