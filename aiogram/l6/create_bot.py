from random import randrange

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from common.variables import DESCRIPTION, HELP, TOKEN
from keyboards.inline_kb.buttons import ikb
from keyboards.kb.buttons import kb_pict, kb_start

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(Text(equals='Random picture'))
async def open_pict_kb(msg: types.Message):
    await msg.delete()
    await msg.answer(
        text='Press the "Get picture" button',
        reply_markup=kb_pict,
    )


@dp.message_handler(Text(equals='Main menu'))
async def open_main_menu_kb(msg: types.Message):
    await msg.delete()
    await msg.answer(
        text='Main menu',
        reply_markup=kb_start,
    )


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await msg.delete()
    await bot.send_sticker(
        chat_id=msg.chat.id,
        sticker='CAACAgQAAxkBAAEGeoljeic8IEQvEB4mTRRw-vEJ0Dp4oQACDwEAAnscSQABwsUhzu1jaHIrBA',
        reply_markup=kb_start,
    )


@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await msg.delete()
    await msg.answer(
        text=HELP,
        parse_mode='HTML',
    )


@dp.message_handler(commands=['desc'])
async def desc_cmd(msg: types.Message):
    await msg.delete()
    await msg.answer(
        text=DESCRIPTION,
    )
    await bot.send_sticker(
        chat_id=msg.chat.id,
        sticker='CAACAgQAAxkBAAEGep5jei2OUcWHDwaQt82fKJjzQThyagACCgEAAnscSQABQaci5QMnwd8rBA'
    )


@dp.message_handler(Text(equals='Get picture'))
async def pict_cmd(msg: types.Message):
    await msg.delete()
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=f'https://picsum.photos/seed/{randrange(1, 1000)}/1920/1080.jpg',
        caption='do you like this photo?',
        reply_markup=ikb,
    )


@dp.callback_query_handler()
async def pict_cb(cb: types.CallbackQuery):
    if cb.data == 'like':
        await cb.answer('like')

    elif cb.data == 'dislike':
        await cb.answer('dislike')

    else:
        await cb.message.edit_media(
            types.InputMedia(
                media=f'https://picsum.photos/seed/{randrange(1, 1000)}/1920/1080.jpg',
                type='photo',
                caption='do you like this photo?',
            ),
            reply_markup=ikb,
        )
        await cb.answer()
