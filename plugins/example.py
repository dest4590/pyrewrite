from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix

@Client.on_message(filters.command('exm', prefixes=prefix.symbol) & filters.me)
async def exm(client: Client, message: Message):
    await message.edit('Пример команды')