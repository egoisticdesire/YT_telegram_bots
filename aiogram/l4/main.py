import os
from random import randrange

from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

load_dotenv(find_dotenv('.tokens'))
TOKEN = os.getenv('aiogramEgo_bot')
DESCRIPTION = '''
This bot is my first bot...
He can send a random letter of English alphabet!
'''
HELP = '''
<b>/start</b> - <em>запуск бота</em>
<b>/desc</b> - <em>описание бота</em>
<b>/pict</b> - <em>показать картинку</em>
<b>/loc</b> - <em>показать локацию</em>
<b>/help</b> - <em>список команд</em>
'''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# Задача: создать клавиатуру
kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    # one_time_keyboard=True,
)
help_btn = KeyboardButton(text='/help')
desc_btn = KeyboardButton(text='/desc')
photo_btn = KeyboardButton(text='/pict')
sticker_btn = KeyboardButton(text='❤️')
loc_btn = KeyboardButton(text='/loc')

kb.add(desc_btn).insert(photo_btn).insert(sticker_btn).add(loc_btn).add(help_btn)


async def on_startup(_):
    print('Bot is online!')


# Задача: команда старт отправляет личное сообщение пользователю и открывает у него клавиатуру
@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await bot.send_message(
        chat_id=msg.from_user.id,
        text='Hey!',
        reply_markup=kb,
    )


@dp.message_handler(commands=['desc'])
async def desc_cmd(msg: types.Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=DESCRIPTION,
    )
    await msg.delete()


@dp.message_handler(commands=['pict'])
async def send_photo_cmd(msg: types.Message):
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo='https://i.picsum.photos/id/25/5000/3333.jpg?hmac=yCz9LeSs-i72Ru0YvvpsoECnCTxZjzGde805gWrAHkM'
    )
    await msg.delete()


# Задача: отправить случайные координаты
@dp.message_handler(commands=['loc'])
async def send_location_cmd(msg: types.Message):
    await bot.send_location(
        chat_id=msg.chat.id,
        latitude=randrange(-90, 90),
        longitude=randrange(-180, 180),
    )
    await msg.delete()


@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=HELP,
        parse_mode='HTML',
        # reply_markup=ReplyKeyboardRemove(),
    )


# Задача: в ответ на сообщение "сердечко" отправить личным сообщением стикер
@dp.message_handler()
async def send_sticker_cmd(msg: types.Message):
    if '❤️' in msg.text:
        await bot.send_sticker(
            chat_id=msg.from_user.id,
            sticker='CAACAgQAAxkBAAEGdRFjdo3VffEFqU5ISaRqTOra_vRP-AACUwEAAnscSQABkGvNmCt56yQrBA',
        )
        await msg.delete()


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
