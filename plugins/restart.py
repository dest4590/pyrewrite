from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import warn
import os
import asyncio

@Client.on_message(filters.command('restart', prefixes=prefix.get()) & filters.me)
async def restart(client: Client, message: Message):
    restart_msg = await warn(message, 'Restarting userbot...', 'time')
    if os.name != 'nt':
        await os.execvp('python3', ['python3','main.py', f'{restart_msg.id},{restart_msg.chat.id}'])
    else:
        await os.execvp('python', ['python','main.py', f'{restart_msg.id},{restart_msg.chat.id}'])

help_menu.add_command('restart', 'Restartes userbot')

@Client.on_message(filters.command('update', prefixes=prefix.get()) & filters.me)
async def update(client, message):
    await warn(message, 'Updating...', 'time')
    
    for command in ['git add *', 'git stash', 'git pull']:
        os.system(command)
        
    await warn(message, 'Done!', 'done')

    await asyncio.sleep(1) # idk

    await restart(client,message)
