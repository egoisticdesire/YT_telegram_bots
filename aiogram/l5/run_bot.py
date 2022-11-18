from aiogram import Bot, Dispatcher, types, executor

# Задача: вынести клавиатуру в отдельный модуль
from common.variables import DESCRIPTION, HELP, TOKEN
from keyboards.inline_kb.buttons import ikb
from keyboards.kb.buttons import kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    print('Bot is online!')


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await bot.send_message(
        chat_id=msg.chat.id,
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


# Задача: показывать инлайн клавиатуру по команде
@dp.message_handler(commands=['links'])
async def desc_cmd(msg: types.Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=DESCRIPTION,
        reply_markup=ikb,
    )
    await msg.delete()


@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await bot.send_message(
        chat_id=msg.chat.id,
        text=HELP,
        parse_mode='HTML',
    )


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
