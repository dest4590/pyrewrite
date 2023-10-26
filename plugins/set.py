from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import cfg
from utils.settings import settings
from plugins.restart import restart
from utils.helpers import getArgs, warn

@Client.on_message(filters.command('set', prefixes=prefix.symbol) & filters.me)
async def setcmd(client: Client, message: Message):
    args = getArgs(message)

    try:
        args[0] # set name
    except IndexError:
        await warn(message, 'Выберите настройку!')
        return

    try:
        args[1] # set value
    except IndexError:
        await warn(message, 'Введите новое значение настройки!')
        return

    if args[0] == 'prefix':
        cfg.sets[args[0]] = args[1]
        await restart(client, message)
    
    else:        
        cfg.sets[args[0]] = args[1]

    await warn(message, f'<b>Настройка: </b><code>{args[0]}</code> <b>была установлена на: </b> <code>{args[1]}</code>', 'done', True)

help_menu.command('set', 'Установить значение настройки')

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
                await warn(message, f'Настройка {cmd_found.get_name()} сброшенна на обычное значение', 'done')
                return

        if cmd_found is None:
            await warn(message, 'Настройка не найдена!')

        else:
            await message.edit(f'<code>{cmd_found}</code> - <b>{cmd_found.get_long_desc()}</b>\n<b>Текущее значение:</b> <code>{cmd_found.get_value()}</code>\n<b>Обычное значение: </b><code>{cmd_found.get_default_value()}</code>')

help_menu.command('sets', 'получить настройки', 'получить список настроек', f'<code>{prefix}sets</code> <code><u>(setting)</u></code> <code>reset</code> <b></i>- чтобы сбросить настройку</i></b>')
