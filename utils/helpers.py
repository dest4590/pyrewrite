import random
import os

from pyrogram.types import Message
from pyrogram import Client

def getArgs(message: Message):
    return str(message.text).split(' ')[1:]

async def warn(message: Message, text: str, warn_type: str = 'error', raw: bool = False):
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

async def sendAsFile(client: Client, message: Message, longText: str):
    await warn(message, 'Ошибка: Сообщение слишком длинное!\Отправляю как файл...')

    with open('./output.txt', 'w', encoding='utf-8', errors='ignore') as out:
        out.write(longText)
    
    await client.send_document(message.chat.id, './output.txt')
    
    os.remove('./output.txt')

def textAnim(text: str):
    """
    Text Animation

    Parameters:
        text (str):
            Text to animate
    """
    symbols = ['*', '@', '#', '$', '%', '^', '&', '&']
    text = text + text[0]
    cipher = [random.choice(symbols) for _ in range(len(text))]
    steps = []
    
    for char in enumerate(text):
        cipher.pop(char[0])
        steps.append(''.join(cipher))
        cipher.insert(char[0], char[1])
        
    return steps

def RawRestart():
    if os.name != 'nt':
        os.execvp('python3', ['python3','main.py'])
    else:
        os.execvp('python', ['python','main.py'])