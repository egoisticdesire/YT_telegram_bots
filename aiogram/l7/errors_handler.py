import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked

from common.variables import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message) -> None:
    await asyncio.sleep(10)
    await msg.answer('some text')


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked_handler(update: types.Update, exception: BotBlocked) -> bool:
    print('you are blocked')
    return True


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
