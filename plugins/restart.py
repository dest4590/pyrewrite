import asyncio
import os

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn
from utils.i18n import i18n

@Client.on_message(filters.command('restart', prefixes=prefix.symbol) & filters.me)
async def restart(client: Client, message: Message):
    restart_message = await warn(message, i18n.get['cmds']['restart-module-message'], 'time')

    if os.name != 'nt':
        await os.execvp('python3', ['python3','main.py', f'{restart_message.id},{restart_message.chat.id}'])
    else:
        await os.execvp('python', ['python','main.py', f'{restart_message.id},{restart_message.chat.id}'])

help_menu.command('restart', i18n.get['cmds']['restart-module-help-short-desc'])

@Client.on_message(filters.command('update', prefixes=prefix.symbol) & filters.me)
async def update(client, message):
    await warn(message, i18n.get['cmds']['update-module-message'], 'time')

    if not os.path.isdir('.git'):
        await warn(message, i18n.get['cmds']['update-module-git-error'])
    
    for command in ['git add *', 'git stash', 'git pull']:
        os.system(command)
        
    await warn(message, i18n.get['cmds']['done'], 'done')

    await asyncio.sleep(1)

    await restart(client, message)

help_menu.command('update', i18n.get['cmds']['update-module-help-short-desc'], i18n.get['cmds']['update-module-help-long-desc'])