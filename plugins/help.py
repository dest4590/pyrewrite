from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn

@Client.on_message(filters.command('help', prefixes=prefix.symbol) & filters.me)
async def info(client: Client, message: Message):
    args = getArgs(message)

    try:
        args[0]
    except IndexError:
        await message.edit(help_menu.get())
    else:
        cmdFound = help_menu.getByName(args[0])
        if cmdFound is None:
            await warn(message, 'Command not found!')

        else:
            await message.edit(f'<code>{prefix}{cmdFound}</code> - <b>{cmdFound.getLongDesc()}\nUsage: </b>\n{cmdFound.getUsage()}')