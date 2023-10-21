from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu

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

help_menu.command('del', 'Deletes message', 'Deletes message that you reply')