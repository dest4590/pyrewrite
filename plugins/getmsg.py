from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn

@Client.on_message(filters.command('getmsg', prefixes=prefix.symbol) & filters.me)
async def getmessage(client: Client, message: Message):
    try:
        getArgs(message)[0]
    except IndexError:
        print(message)
        await warn(message, 'Done!', 'done')
    else:
        await warn(message, f'✅ <b>Done</b>: <code>{message}</code>', 'done', True)

help_menu.command('getmessage', 'Get message data', 'Send all message data to terminal (json, pyrogram)')