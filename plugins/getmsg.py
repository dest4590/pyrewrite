from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn, sendAsFile

@Client.on_message(filters.command('getmsg', prefixes=prefix.symbol) & filters.me)
async def getmessage(client: Client, message: Message):
    try:
        getArgs(message)[0]
    except IndexError:
        print(message)
        await warn(message, f'Получено сообщение: {message.id}!', 'done')
    else:
        await warn(message, '<b>Готово\nОтправляю как файл...</b>', 'done', True)
        await sendAsFile(client, message, str(message))

help_menu.command('getmsg', 'Получить информацию об сообщении', 'Отправляет всю информацию об сообщении (json, pyrogram)')