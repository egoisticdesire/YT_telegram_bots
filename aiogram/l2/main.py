import os
import random
import string
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types, executor

load_dotenv(find_dotenv('.tokens'))
TOKEN = os.getenv('aiogramEgo_bot')
HELP = '''
/start - запуск бота
/description - описание бота
/count - считает количество своих вызовов
/help - список команд
'''
DESCRIPTION = '''
This bot is my first bot...
He can send a random letter of English alphabet!
'''

count = 0

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await msg.answer(text='Welcome!')
    await msg.delete()


# Задача: добавить команду /description, выводящую описание бота
@dp.message_handler(commands=['description'])
async def description_cmd(msg: types.Message):
    await msg.reply(text=DESCRIPTION)


# Задача: добавить команду /count, выводящую количество собственных вызовов
@dp.message_handler(commands=['count'])
async def count_cmd(msg: types.Message):
    global count
    count += 1
    await msg.reply(text=f'The "count" command was called {count} times')


@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await msg.reply(text=HELP)


# Задача: отвечать на сообщение пользователя случайным символом алфавита
# Задача: отвечать на сообщение пользователя YES, если сообщение содержит 0, иначе - NO
@dp.message_handler()
async def common_cmd(msg: types.Message):
    await msg.reply(text=f'This is a random ASCII letter: "{random.choice(string.ascii_letters)}"')
    await msg.answer(text='YES' if '0' in msg.text else 'NO')


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
