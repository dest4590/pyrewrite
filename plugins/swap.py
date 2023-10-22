from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import warn, RawRestart
from utils.config import cfg
from glob import glob

@Client.on_message(filters.command('swap', prefixes=prefix.symbol) & filters.me)
async def swap(client: Client, message: Message):
    swap_session = ''
    for session in glob('*.session'):
        if session != f'{cfg.sets["session"]}.session':
            swap_session = session
            break

    cfg.sets['session'] = swap_session.replace('.session', '')
    await warn(message, f'Меняем аккаунт на: <code>{swap_session}</code>\nПерезагружаем юсербота...', 'done')
    RawRestart()

help_menu.command('swap', 'Меняет аккаунт на другой', 'Меняет сессию pyrogram на другую (лучше всего использовать с 2 сессиями)')