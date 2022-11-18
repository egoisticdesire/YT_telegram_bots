from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Задача: создать обычную клавиатуру для вызова команды /links
kb = ReplyKeyboardMarkup(resize_keyboard=True)

links_btn = KeyboardButton(text='/links')
desc_btn = KeyboardButton(text='/desc')
help_btn = KeyboardButton(text='/help')

kb.row(links_btn, desc_btn).add(help_btn)
