from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import cfg
from utils.settings import settings
from plugins.restart import restart
from utils.helpers import getArgs, warn
from utils.i18n import i18n

@Client.on_message(filters.command('set', prefixes=prefix.symbol) & filters.me)
async def setcmd(client: Client, message: Message):
    args = getArgs(message)

    try:
        args[0] # set name
    except IndexError:
        await warn(message, i18n.get['cmds']['set-module-choose-setting'])
        return

    try:
        args[1] # set value
    except IndexError:
        await warn(message, i18n.get['cmds']['set-module-enter-new-value'])
        return

    if args[0] == 'prefix':
        cfg.sets[args[0]] = args[1]
        await restart(client, message)
    
    else:        
        cfg.sets[args[0]] = args[1]

    await warn(message, i18n.get['cmds']['set-module-setting-set'].format(args[0], args[1]), 'done', True)

help_menu.command('set', i18n.get['cmds']['set-module-help-short-desc'])

@Client.on_message(filters.command('sets', prefixes=prefix.symbol) & filters.me)
async def sets(client: Client, message: Message):
    args = getArgs(message)
    
    try:
        args[0]
    except IndexError:
        await message.edit(settings.get(), disable_web_page_preview=True)
    else:
        cmd_found = settings.get_by_name(args[0])
        
        try:
            args[1]
        except IndexError:
            pass
        else:
            if args[1] == 'reset':
                cmd_found.set_default_value()
                await warn(message, i18n.get['cmds']['sets-module-setting-reset'].format(cmd_found.get_name()), 'done')
                return

        if cmd_found is None:
            await warn(message, i18n.get['cmds']['sets-module-setting-not-found'])

        else:
            await message.edit(i18n.get['cmds']['sets-module-output'].format(cmd_found, cmd_found.get_long_desc(), cmd_found.get_value(), cmd_found.get_default_value()))

help_menu.command('sets', i18n.get['cmds']['sets-module-help-short-desc'], i18n.get['cmds']['sets-module-help-long-desc'], i18n.get['cmds']['sets-module-help-usage'].format(prefix, ))
