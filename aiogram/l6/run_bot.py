"""
Реализовать минимум три команды /pict, /description, /help и добавить их в меню клавиатуры.
Реализовать меню, в котором можно вызвать случайную картинку из списка.
Реализовать описание к фотографии, а также кнопки инлайн клавиатуры (лайк/дизлайк).
    При нажатии на кнопки генерировать callback запрос и обрабатывать запрос на стороне сервера.
Реализовать кнопку, выводящую следующую случайную фотографию.
Реализовать отправку стикеров.
"""

from aiogram.utils import executor

from create_bot import dp


async def on_startup(_):
    print('Bot is online!')


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
