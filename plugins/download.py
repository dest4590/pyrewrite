from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn
import requests
import os

@Client.on_message(filters.command('download', prefixes=prefix.symbol) & filters.me)
async def download_cmd(client: Client, message: Message):
    if message.reply_to_message is None:
        args = getArgs(message)
        link = args[0]
        await warn(message, 'Downloading...', 'time')
        
        try:
            file = requests.get(link).content
        except Exception as e:
            await warn(message, f'<b>Error:</b> <code>{e}</code>', raw=True)
            return
        file_name = os.path.basename(link)

        with open(file_name, 'wb') as s:
            s.write(file)

        await warn(message, 'Downloaded!', 'done')

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

                await warn(message, 'Downloading...', 'time')
                
                file = requests.get(link).content


                with open(file_name, 'wb') as s:
                    s.write(file)

                await warn(message, 'Downloaded!', 'done')
                await client.send_document(message.chat.id, file_name)

                os.remove(file_name)

help_menu.command('download', 'Download by link', 'Download and send file by link')