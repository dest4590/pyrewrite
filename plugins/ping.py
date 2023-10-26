from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu

@Client.on_message(filters.command('ping', prefixes=prefix.symbol) & filters.me)
async def ping(client: Client, message: Message):
    start_time = datetime.now()
    
    await message.edit('<b>⏳ Загрузка...</b>')
    
    end_time = datetime.now()
    
    ping_time = (end_time - start_time).microseconds / 1000 # Calculate ping

    await message.edit(f'<b>⏳ Пинг:</b> <code>{ping_time} миллисекунд</code>')

help_menu.command('ping', 'проверка пинга', 'Проверить пинг с серверами Telegram')
