from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.restart import restart
from plugins.helpers import warn
import os

@Client.on_message(filters.command('dlmod', prefixes=prefix.get()) & filters.me)
async def dlmod(client: Client, message: Message):
    if message.reply_to_message != None:
        if message.reply_to_message.document != None:
            await warn(message, 'Downloading...', 'time')

            await client.download_media(message.reply_to_message, './plugins/custom/'+os.path.basename(message.reply_to_message.document.file_name))
            
            await warn(message, 'Done!', 'done')
            
            await restart(client, message)
        else:
            await warn(message, 'The message must be a file!')
    else:
        await warn(message, 'Reply to message!')

help_menu.add_command('dlmod', 'download module')