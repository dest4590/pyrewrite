from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.settings import settings
from utils.config import cfg
from utils.helpers import getArgs, textAnim
from pyrogram.errors import FloodWait
from asyncio import sleep

@Client.on_message(filters.command('type', prefixes=prefix.symbol) & filters.me)
async def type(client: Client, message: Message):
    text = getArgs(message)
    
    try:
        type_delay = float(cfg.sets['type_delay', '0.05'])
    except IndexError:
        type_delay = 0.05

    for i in textAnim(' '.join(text)):
        try:
            await message.edit(i + '</b>')
        except FloodWait as wait:
            await sleep(wait.value)

        await sleep(type_delay)

@Client.on_message(filters.me)
async def make_type(client: Client, message: Message):
    if cfg.sets['type', 'f'] == 't':
        message.text = '.type ' + message.text
        await type(client, message)

help_menu.command('type', 'Typing animation', 'Make animation when you send message')
settings.add('type', 'typing animation', 'enable .type animation (t, f)', 'f')
settings.add('type_delay', 'how many time to wait (float, with dots)', default_value='0.05')