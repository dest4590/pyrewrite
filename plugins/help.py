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
        cmd_found = help_menu.get_by_name(args[0])
        if cmd_found is None:
            await warn(message, 'Команда не найдена!')

        else:
            await message.edit(f'<code>{prefix}{cmd_found}</code> - <b>{cmd_found.get_long_desc()}\nUsage: </b>\n{cmd_found.get_usage()}')