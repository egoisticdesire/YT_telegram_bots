from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from common.variables import TOKEN, DESCRIPTION, HELP

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
cb = CallbackData('ikb', 'action')


def get_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Description', callback_data=cb.new('ibtn_description')),
                InlineKeyboardButton(text='Help', callback_data=cb.new('ibtn_help')),
            ],
        ]
    )


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message) -> None:
    await msg.answer(
        text='Welcome to my first Aiogram Bot!',
        reply_markup=get_inline_keyboard(),
    )


@dp.message_handler(commands=['desc'])
async def description_cmd(msg: types.Message) -> None:
    await msg.answer(
        text=DESCRIPTION,
    )


@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message) -> None:
    await msg.answer(
        text=HELP,
        parse_mode='html',
    )


@dp.callback_query_handler(cb.filter(action='ibtn_description'))
async def description_ikb_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        text=DESCRIPTION,
    )
    await callback.answer()


@dp.callback_query_handler(cb.filter(action='ibtn_help'))
async def help_ikb_cb_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(
        text=HELP,
        parse_mode='html'
    )
    await callback.answer()
