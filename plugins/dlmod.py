from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.restart import restart
from utils.helpers import warn
import os

@Client.on_message(filters.command('dlmod', prefixes=prefix.symbol) & filters.me)
async def dlmod(client: Client, message: Message):
    if message.reply_to_message is not None:
        if message.reply_to_message.document is not None:
            await warn(message, 'Downloading...', 'time')

            await client.download_media(message.reply_to_message, './plugins/custom/'+os.path.basename(message.reply_to_message.document.file_name))
            
            await warn(message, 'Done!', 'done')
            
            await restart(client, message)
        else:
            await warn(message, 'The message must be a file!')
    else:
        await warn(message, 'Reply to message!')

help_menu.command('dlmod', 'download module')