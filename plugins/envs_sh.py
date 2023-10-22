from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn, getArgs
import requests
import os

@Client.on_message(filters.command('upload', prefixes=prefix.symbol) & filters.me)
async def upload_command(client: Client, message: Message):
    try:
        getArgs(message)[0]
    except IndexError:
        send = False
    else:
        send = True
    
    if message.reply_to_message is not None:
        await warn(message, 'Выкладываем...', 'time')

        downloaded_media = await client.download_media(message.reply_to_message, './')

        envs = requests.post(
                    "http://envs.sh",
                    files={"file": open(downloaded_media, 'rb').read()},
        )

        await warn(message, f'<b>Готово!\nСсылка: </b><code>{envs.text}</code>', 'done', raw=True)
        
        if send:
            await client.send_message(message.chat.id, envs.text)

        os.remove('./' + os.path.basename(downloaded_media))
    
    elif message.reply_to_message is None:
        await warn(message, 'Ответьте на сообщение с медиа!')


help_menu.command('upload', 'выкладывает видео', 'Выкладывает видео на envs.sh', f'{prefix}upload\n{prefix}upload true (для того, чтобы ссылка отправилась после выкладывания)')