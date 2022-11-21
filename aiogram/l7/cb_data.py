from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from common.variables import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

cb = CallbackData('ikb', 'action')

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='button', callback_data=cb.new('push'))
        ]
    ]
)


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message) -> None:
    await msg.answer(
        text='some text',
        reply_markup=ikb,
    )


@dp.callback_query_handler(cb.filter())
async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['action'] == 'push':
        await callback.answer('something!')


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
