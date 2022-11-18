import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('.tokens'))

TOKEN = os.getenv('aiogramEgo_bot')

DESCRIPTION = '''
This bot is my first bot...
'''

HELP = '''
<b>/start</b> - <em>запуск бота</em>
<b>/desc</b> - <em>описание бота</em>
<b>/links</b> - <em>показать ссылки</em>
<b>/help</b> - <em>список команд</em>
'''
