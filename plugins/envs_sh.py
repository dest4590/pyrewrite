from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from plugins.helpers import warn, get_args
import requests
import os

@Client.on_message(filters.command('upload', prefixes=prefix.get()) & filters.me)
async def upload_command(client: Client, message: Message):
    try:get_args(message)[0]
    except IndexError:send = False
    else:
        send = True
    
    if message.reply_to_message != None:
        await warn(message, 'Uploading...', 'time')

        downloaded_media = await client.download_media(message.reply_to_message, './')

        envs = requests.post(
                    "http://envs.sh",
                    files={"file": open(downloaded_media, 'rb').read()},
        )

        await warn(message, f'<b>Done!\nLink: </b>{envs.text}', 'done', raw=True)
        
        if send:
            await client.send_message(message.chat.id, envs.text)

        os.remove('./' + os.path.basename(downloaded_media))
    
    elif message.reply_to_message == None:
        await warn(message, 'Reply to message with media!')


help_menu.add_command('upload', 'upload media to site', 'Uploads media to a envs.sh', f'{prefix.get()}upload\n{prefix.get()}upload true (for send link after upload)')