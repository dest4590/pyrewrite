import os as __os

from pyrogram import Client as __Client
from pyrogram.types import Message as __Message

from utils.i18n import i18n


def getArgs(message: __Message):
    return str(message.text).split(' ')[1:]

async def warn(message: __Message, text: str, warn_type: str = 'error', raw: bool = False):
    """
    Warn/Info about command

    Parameters:
        message (:obj:`~pyrogram.types.Message`):
            Pyrogram Message

        text (str, *optional*):
            Text to show

        type (str, *optional*):
            Type of the message. Can be 'error', 'info', 'time', or 'done'. Defaults to 'error'.

        raw (bool, *optional*):
            Controls the formatting of the message. If True, the message is sent without HTML formatting. Defaults to False.
    """

    emojis = {
        'error': '❌',
        'info': 'ℹ',
        'time': '⏳',
        'done': '✅',
    }

    if raw:
        await message.edit(f'{emojis[warn_type] if raw is False else ""} {text[0].upper() + text[1:]}', disable_web_page_preview=True)
    else:
        await message.edit(f'{emojis[warn_type] if raw is False else ""} <b>{text[0].upper() + text[1:]}</b>', disable_web_page_preview=True)

    return message

async def sendAsFile(client: __Client, message: __Message, longText: str):
    await warn(message, i18n.get['sendAsFile-warning'])

    with open('./output.txt', 'w', encoding='utf-8', errors='ignore') as out:
        out.write(longText)
    
    await client.send_document(message.chat.id, './output.txt')
    
    __os.remove('./output.txt')

def raw_restart():
    if __os.name != 'nt':
        __os.execvp('python3', ['python3','main.py'])
    else:
        __os.execvp('python', ['python','main.py'])