from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=2)

like_ibtn = InlineKeyboardButton(
    text='👍',
    callback_data='like',
)
dislike_ibtn = InlineKeyboardButton(
    text='👎',
    callback_data='dislike'
)
next_ibtn = InlineKeyboardButton(
    text='Get picture',
    callback_data='next_pict'
)

ikb.add(like_ibtn, dislike_ibtn).add(next_ibtn)
