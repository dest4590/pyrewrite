from glob import glob

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn, raw_restart
from utils.i18n import i18n
from utils.config import cfg

@Client.on_message(filters.command('swap', prefixes=prefix.symbol) & filters.me)
async def swap(client: Client, message: Message):
    swap_session = ''
    for session in glob('*.session'):
        if session != f'{cfg.sets["session"]}.session':
            swap_session = session
            break

    cfg.sets['session'] = swap_session.replace('.session', '')

    await warn(message, i18n.get['cmds']['swap-module-account-change'].format(swap_session), 'done')
    raw_restart()

help_menu.command('swap', i18n.get['cmds']['swap-module-help-short-desc'], i18n.get['cmds']['swap-module-help-long-desc'])