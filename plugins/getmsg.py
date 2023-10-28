from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.i18n import i18n
from utils.helpers import getArgs, warn, sendAsFile

@Client.on_message(filters.command('getmsg', prefixes=prefix.symbol) & filters.me)
async def getmessage(client: Client, message: Message):
    try:
        getArgs(message)[0]
    except IndexError:
        print(message)
        await warn(message, i18n.get['cmds']['getmsg-module-output'].format(message.id), 'done')
    else:
        await warn(message, i18n.get['cmds']['getmsg-module-asfile'], 'done', True)
        await sendAsFile(client, message, str(message))

help_menu.command(
    'getmsg', 
    i18n.get['cmds']['getmsg-module-help-short-desc'], 
    i18n.get['cmds']['getmsg-module-help-long-desc']
)
