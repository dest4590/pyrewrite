from pyrogram import Client, filters
from pyrogram.types import Message

from utils.help import help_menu
from utils.i18n import i18n
from utils.prefix import prefix


@Client.on_message(filters.command('del', prefixes=prefix.symbol) & filters.me)
async def delete(client: Client, message: Message):
    if message.chat.id != message.from_user.id:
        if message.outgoing:
            if message.reply_to_message is not None:
                await message.reply_to_message.delete()
            await message.delete()

    else:
        if message.reply_to_message is not None:
            await message.reply_to_message.delete()
            
        await message.delete()

help_menu.command('del', i18n.get['cmds']['del-module-help-short-desc'], i18n.get['cmds']['del-module-help-long-desc'])