import os

from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.restart import restart
from utils.help import help_menu
from utils.helpers import warn
from utils.i18n import i18n
from utils.prefix import prefix


@Client.on_message(filters.command('dlmod', prefixes=prefix.symbol) & filters.me)
async def dlmod(client: Client, message: Message):
    if message.reply_to_message is not None:
        if message.reply_to_message.document is not None:
            await warn(message, i18n.get['cmds']['dlmod-module-message'], 'time')

            await client.download_media(message.reply_to_message, './plugins/custom/' + os.path.basename(message.reply_to_message.document.file_name))
            
            await warn(message, i18n.get['cmds']['done'], 'done')
            
            await restart(client, message)
        else:
            await warn(message, i18n.get['cmds']['dlmod-module-error-file'])
    else:
        await warn(message, i18n.get['cmds']['dlmod-module-error-reply'])

help_menu.command('dlmod', i18n.get['cmds']['dlmod-module-help-short-desc'])