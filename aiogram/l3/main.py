import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types, executor

load_dotenv(find_dotenv('.tokens'))
TOKEN = os.getenv('aiogramEgo_bot')

# Задача: команды - жирным шрифтом, описание - курсивом
HELP = '''
<b>/start</b> - <em>запуск бота</em>
<b>/give</b> - <em>получить стикер</em>
<b>/help</b> - <em>список команд</em>
'''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


# Задача: уведомить о запуске бота
async def on_startup(_):
    print('Bot is online!')


@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await msg.answer(text='<em><b>Welcome!</b></em>', parse_mode='HTML')


# Задача: ответить сообщением, а потом отправить стикер
@dp.message_handler(commands=['give'])
async def give_cmd(msg: types.Message):
    await msg.reply(text="It's funny 😁")
    await bot.send_sticker(
        msg.from_user.id,
        sticker='CAACAgQAAxkBAAEGdRFjdo3VffEFqU5ISaRqTOra_vRP-AACUwEAAnscSQABkGvNmCt56yQrBA',
    )


# Задача: отправить ID использованного стикера
@dp.message_handler(content_types=['sticker'])
async def get_sticker_id(msg: types.Message):
    await msg.reply(text=f'Sticker ID:\n{msg.sticker.file_id}')


@dp.message_handler(commands=['help'])
async def help_cmd(msg: types.Message):
    await msg.reply(text=HELP, parse_mode='HTML')


# Задача: если сообщение содержит эмодзи "сердце", ответить "черным сердцем"
# Задача: если сообщение содержит эмодзи "галочка", подсчитать их количество
@dp.message_handler()
async def echo_cmd(msg: types.Message):
    if '❤️' in msg.text:
        await msg.reply(text='🖤')
    if '✅' in msg.text:
        await msg.reply(text=f"✅ x{str(msg.text.count('✅'))}")


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
