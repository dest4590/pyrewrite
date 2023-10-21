from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn

@Client.on_message(filters.command('quit', prefixes=prefix.symbol) & filters.me)
async def quit_cmd(client: Client, message: Message):
    await warn(message, '👋 <b>Userbot stopped</b>', raw=True)
    quit()

help_menu.command('quit', 'Quit from userbot')