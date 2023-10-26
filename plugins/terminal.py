import os

from pyrogram import Client, filters
from pyrogram.types import Message
import pyrogram.errors
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn, sendAsFile

@Client.on_message(filters.command('terminal', prefixes=prefix.symbol) & filters.me)
async def exm(client: Client, message: Message):
    args = getArgs(message)
    
    await warn(message, 'Выполнение...', 'time')

    output = os.popen(' '.join(args)).read()
    
    try:
        await warn(message, f'<b>Готово:</b>\n<b>Команда:\n</b><code>{" ".join(args)}</code> <code>\n{output}</code>', 'done', raw=True)

    except pyrogram.errors.exceptions.bad_request_400.MessageTooLong:
        await sendAsFile(client, message, output)

help_menu.command('terminal', 'Терминал', 'Простой терминал')