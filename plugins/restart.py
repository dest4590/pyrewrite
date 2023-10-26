import asyncio
import os

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn

@Client.on_message(filters.command('restart', prefixes=prefix.symbol) & filters.me)
async def restart(client: Client, message: Message):
    restart_message = await warn(message, 'Перезагрузка юсербота...', 'time')
    if os.name != 'nt':
        await os.execvp('python3', ['python3','main.py', f'{restart_message.id},{restart_message.chat.id}'])
    else:
        await os.execvp('python', ['python','main.py', f'{restart_message.id},{restart_message.chat.id}'])

help_menu.command('restart', 'Перезапускает юсербота')

@Client.on_message(filters.command('update', prefixes=prefix.symbol) & filters.me)
async def update(client, message):
    await warn(message, 'Обновление...', 'time')

    if not os.path.isdir('.git'):
        await warn(message, 'Юсербот установлен не через git, обновление невозможно\nПожалуйста, установите юсербота через git!')
    
    for command in ['git add *', 'git stash', 'git pull']:
        os.system(command)
        
    await warn(message, 'Готово!', 'done')

    await asyncio.sleep(1)

    await restart(client, message)

help_menu.command('update', 'обновить юсербота', 'Обновляет юсербота через Git (требует установку через git clone)')