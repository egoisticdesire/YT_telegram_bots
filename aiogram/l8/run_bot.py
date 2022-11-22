from aiogram import executor
from create_bot import dp


async def on_startup(_) -> None:
    print('Bot is online!')


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_startup,
    )
