from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from datetime import datetime

@Client.on_message(filters.command('ping', prefixes=prefix.symbol) & filters.me)
async def ping(client: Client, message: Message):
    start_time = datetime.now()
    await message.edit('<b>⏳ Loading...</b>')
    end_time = datetime.now()
    ping_time = (end_time - start_time).microseconds / 1000

    await message.edit(f'<b>⏳ Ping:</b> <code>{ping_time} ms</code>')

help_menu.command('ping', 'Ping Pong', 'Check ping')
