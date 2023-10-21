from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import cfg
import platform
import os
import sys

system = 'Linux 🐧' if os.name == 'posix' else 'Windows 💻'

if os.name == 'posix':
    if 'termux' in sys.executable.lower():
        system = 'Termux 📱'
    else:
        import distro
        system = distro.name(pretty=False)

default = f'''
<b><a href="https://github.com/purpl3-yt/pyrewrite">PyRewrite</a> - Simple & Convenient</b>
<b>🖌 Prefix:</b> <b>"</b><code>{prefix}</code><b>"</b>
<b>🖥 OS: {system}</b>
<b>💻 Hosted on: {platform.node()}</b>
<b>🔧 Commands: {str(help_menu.getLen())}</b>
<b>📦 Built-in Plugins: {str(help_menu.getLenBuildin())}</b>
<b>🔌 Custom Plugins: {str(help_menu.getLenCustom())}</b>
<b>🛠 Modules channel: @pyrewrite</b>'''

def get_info_menu(info_type = 'full'):
    if info_type == 'full':
        return default

    elif info_type == 'lite':
        return f'''
<b><a href="https://github.com/purpl3-yt/pyrewrite">PyRewrite</a> Info Menu</b>
<b>🖌 Prefix:</b> <b>"</b><code>{prefix}</code><b>"</b>
<b>🔧 Commands: {str(help_menu.getLen())}</b>
<b>🛠 Modules channel: @pyrewrite</b>'''
    
    else: 
        return default

@Client.on_message(filters.command('info', prefixes=prefix.symbol) & filters.me)
async def info(client: Client, message: Message):
    chat_id = message.chat.id
    await message.delete()
    
    if message.reply_to_message is not None:
        await client.send_animation(chat_id, cfg.sets['banner', 'https://envs.sh/hkf.mp4'], get_info_menu(cfg.sets['info']), reply_to_message_id=message.reply_to_message.id)
    
    else:
        await client.send_animation(chat_id, cfg.sets['banner', 'https://envs.sh/hkf.mp4'], get_info_menu(cfg.sets['info']))
    

help_menu.command('info', 'Get info', 'Get info about userbot')