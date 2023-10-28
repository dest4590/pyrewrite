import os

from pyrogram import Client, filters
from pyrogram.types import Message
import pyrogram.errors
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn, sendAsFile
from utils.i18n import i18n

@Client.on_message(filters.command('terminal', prefixes=prefix.symbol) & filters.me)
async def exm(client: Client, message: Message):
    args = getArgs(message)
    
    await warn(message, i18n.get['cmds']['terminal-module-executing'], 'time')

    output = os.popen(' '.join(args)).read()
    
    try:
        await warn(message, i18n.get['cmds', 'terminal-module-output'].format(" ".join(args), output), 'done', raw=True)

    except pyrogram.errors.exceptions.bad_request_400.MessageTooLong:
        await sendAsFile(client, message, output)

help_menu.command('terminal', 'Терминал', 'Простой терминал')