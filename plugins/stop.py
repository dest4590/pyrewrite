import sys

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn

@Client.on_message(filters.command('stop', prefixes=prefix.symbol) & filters.me)
async def stop(client: Client, message: Message):
    await warn(message, '👋 <b>Юсербот остановлен</b>', raw=True)
    sys.exit(1)

help_menu.command('stop', 'Выключить юсербота')