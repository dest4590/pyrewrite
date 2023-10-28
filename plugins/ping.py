from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn
from utils.i18n import i18n

@Client.on_message(filters.command('ping', prefixes=prefix.symbol) & filters.me)
async def ping(client: Client, message: Message):
    start_time = datetime.now()
    
    await warn(message, i18n.get['cmds']['ping-module-loading'])
    
    end_time = datetime.now()
    
    ping_time = (end_time - start_time).microseconds / 1000 # Calculate ping

    await message.edit(i18n.get['cmds']['ping-module-output'].format(ping_time))

help_menu.command('ping', i18n.get['cmds']['ping-module-help-short-desc'], i18n.get['cmds']['ping-module-help-long-desc'])
