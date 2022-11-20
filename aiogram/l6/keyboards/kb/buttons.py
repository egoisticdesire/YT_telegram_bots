from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
pict_menu_btn = KeyboardButton(text='Random picture')
desc_btn = KeyboardButton(text='/desc')
help_btn = KeyboardButton(text='/help')
kb_start.add(pict_menu_btn).add(desc_btn).add(help_btn)

kb_pict = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pict_btn = KeyboardButton(text='Get picture')
back_btn = KeyboardButton(text='Main menu')
kb_pict.add(pict_btn).add(back_btn)

kb_vote = ReplyKeyboardMarkup(resize_keyboard=True)
like_btn = KeyboardButton(text='/like')
dislike_btn = KeyboardButton(text='/dislike')
kb_vote.row(like_btn, dislike_btn)
