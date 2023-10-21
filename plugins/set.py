from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import cfg
from utils.settings import settings
from plugins.restart import restart
from utils.helpers import getArgs, warn

@Client.on_message(filters.command('set', prefixes=prefix.symbol) & filters.me)
async def set(client: Client, message: Message):
    args = getArgs(message)

    try:
        args[0] # set name
    except IndexError:
        await warn(message, 'Choose a setting!')
        return

    try:
        args[1] # set value
    except IndexError:
        await warn(message, 'Enter the setting value!')
        return

    if args[0] == 'prefix':
        cfg.sets[args[0]] = args[1]
        await restart(client, message)
    
    else:
        cfg.sets[args[0]] = args[1]

    await warn(message, f'<b>The setting:</b> <code>{args[0]}</code> <b>is set to: </b> <code>{args[1]}</code>', 'done', True)

help_menu.command('set', 'Set Setting')

@Client.on_message(filters.command('sets', prefixes=prefix.symbol) & filters.me)
async def sets(client: Client, message: Message):
    args = getArgs(message)
    
    try:
        args[0]
    except IndexError:
        await message.edit(settings.get(), disable_web_page_preview=True)
    else:
        cmd_found = settings.getByName(args[0])
        
        try:
            args[1]
        except IndexError:
            pass
        else:
            if args[1] == 'reset':
                cmd_found.setDefaultValue()
                await warn(message, f'Setting {cmd_found.getName()} to default value', 'done')
                return

        if cmd_found is None:
            await warn(message, 'Setting not found!')

        else:
            await message.edit(f'<code>{cmd_found}</code> - <b>{cmd_found.getLongDesc()}</b>\n<b>Current value:</b> <code>{cmd_found.getValue()}</code>\n<b>Default value: </b><code>{cmd_found.getDefaultValue()}</code>')

help_menu.command('sets', 'Get settings', 'Get list of settings', f'<code>{prefix}sets</code> <code><u>(setting)</u></code> <code>reset</code> <b></i>- for reset setting to default value</i></b>')