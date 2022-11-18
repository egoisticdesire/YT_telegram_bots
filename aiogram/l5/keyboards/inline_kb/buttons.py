from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Задача: каждая инлайн кнопка содержит ссылку
ikb = InlineKeyboardMarkup(row_width=2)

google_ibtn = InlineKeyboardButton(
    text='open google',
    url='https://google.com',
)
youtube_ibtn = InlineKeyboardButton(
    text='open youtube',
    url='https://youtube.com',
)

ikb.add(google_ibtn, youtube_ibtn)
