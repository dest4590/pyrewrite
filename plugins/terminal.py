import os

import pyrogram.errors
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.help import help_menu
from utils.helpers import getArgs, sendAsFile, warn
from utils.i18n import i18n
from utils.prefix import prefix


@Client.on_message(filters.command('terminal', prefixes=prefix.symbol) & filters.me)
async def terminal(client: Client, message: Message):
    args = getArgs(message)
    
    await warn(message, i18n.get['cmds']['terminal-module-executing'], 'time')

    output = os.popen(' '.join(args)).read()
    
    try:
        await warn(message, i18n.get['cmds']['terminal-module-output'].format(" ".join(args), output), 'done', raw=True)

    except pyrogram.errors.exceptions.bad_request_400.MessageTooLong:
        await sendAsFile(client, message, output)

help_menu.command('terminal', 'Терминал', 'Простой терминал')