from random import randrange

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.variables import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

is_voted = False

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👍', callback_data='like'), InlineKeyboardButton(text='👎', callback_data='dislike')],
        [InlineKeyboardButton(text='close keyboard', callback_data='close')],
    ]
)


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message) -> None:
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo=f'https://picsum.photos/seed/{randrange(1, 1000)}/1920/1080.jpg',
        caption='like or dislike?',
        reply_markup=ikb,
    )


@dp.callback_query_handler(text='close')
async def ikb_close_cb_handler(cb: types.CallbackQuery) -> None:
    await cb.message.delete()


@dp.callback_query_handler()
async def ikb_common_cb_handler(cb: types.CallbackQuery) -> None:
    global is_voted
    if not is_voted:
        if cb.data == 'like':
            await cb.answer(
                text='like',
            )
            is_voted = True
        await cb.answer(
            text='dislike',
        )
        is_voted = True
    await cb.answer(
        text='already voted'
    )


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
