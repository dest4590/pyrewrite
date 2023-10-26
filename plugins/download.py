import os
import requests

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn

@Client.on_message(filters.command('download', prefixes=prefix.symbol) & filters.me)
async def download_cmd(client: Client, message: Message):
    if message.reply_to_message is None:
        args = getArgs(message)
        link = args[0]
        await warn(message, 'Скачиваем...', 'time')

        try:
            file = requests.get(link, timeout=5).content
        except Exception as e:
            await warn(message, f'<b>Ошибка:</b> <code>{e}</code>', raw=True)
            return
        file_name = os.path.basename(link)

        with open(file_name, 'wb') as s:
            s.write(file)

        await warn(message, 'Скачано!', 'done')

        await client.send_document(message.chat.id, file_name)

        os.remove(file_name)

    elif message.reply_to_message is not None:
        if message.reply_to_message.text is not None:
            link = message.reply_to_message.text

            if link.startswith('https'):

                if link.endswith('/'):
                    link = link[:-1]

                file_name = os.path.basename(link)

                if file_name == '':
                    file_name = 'unknown'

                await warn(message, 'Скачиванием...', 'time')
                
                file = requests.get(link, timeout=5).content

                with open(file_name, 'wb') as s:
                    s.write(file)

                await warn(message, 'Скачано!', 'done')
                await client.send_document(message.chat.id, file_name)

                os.remove(file_name)

help_menu.command('download', 'Скачивает файл', 'Скачивает и отправляет файл по ссылке')