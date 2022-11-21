from random import randrange

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.variables import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
number = 0


def get_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='increase', callback_data='btn_increase'),
                InlineKeyboardButton(text='decrease', callback_data='btn_decrease'),
            ],
            [
                InlineKeyboardButton(text='random value', callback_data='btn_random_value'),
            ]
        ]
    )


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message) -> None:
    await msg.answer(
        text=f'the current number is {number}',
        reply_markup=get_inline_keyboard(),
    )


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn_'))
async def ikb_cb_handler(cb: types.CallbackQuery) -> None:
    global number
    if cb.data == 'btn_increase':
        number += 1
        await cb.message.edit_text(
            text=f'the current number is {number}',
            reply_markup=get_inline_keyboard(),
        )
    elif cb.data == 'btn_decrease':
        number -= 1
        await cb.message.edit_text(
            text=f'the current number is {number}',
            reply_markup=get_inline_keyboard(),
        )
    elif cb.data == 'btn_random_value':
        number = randrange(-1000, 1000)
        await cb.message.edit_text(
            text=f'the current number is {number}',
            reply_markup=get_inline_keyboard(),
        )


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
