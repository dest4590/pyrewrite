from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.config import set_setting
from plugins.restart import restart
from utils.settings import settings
from plugins.helpers import get_args, warn

@Client.on_message(filters.command('set', prefixes=prefix.get()) & filters.me)
async def set(client: Client, message: Message):
    args = get_args(message)

    try:args[0] # set name
    except:await warn(message, 'Enter setting!');return

    try:args[1] # set value
    except IndexError:
        
        if message.reply_to_message == None:
            await warn(message, 'Enter setting value!');return
        
        elif message.reply_to_message != None:
            if message.reply_to_message.text != None:
                set_setting(args[0], message.reply_to_message.text, 'settings')
                
                await warn(message, f'<b>Set setting:</b> <code>{args[0]}</code> <b>to</b> <code>{message.reply_to_message.text}</code>', 'done', True)
            elif message.reply_to_message.caption != None:
                set_setting(args[0], message.reply_to_message.caption, 'settings')
                
                await warn(message, f'<b>Set setting:</b> <code>{args[0]}</code> <b>to</b> <code>{message.reply_to_message.caption}</code>', 'done', True)

            return
    if args[0] == 'prefix':
        set_setting(args[0], args[1], 'main')
        await restart(client, message)
    else:
        set_setting(args[0], args[1], 'settings')

    await warn(message, f'<b>Set setting:</b> <code>{args[0]}</code> <b>to</b> <code>{args[1]}</code>', 'done', True)

help_menu.add_command('set', 'Set Setting')

@Client.on_message(filters.command('sets', prefixes=prefix.get()) & filters.me)
async def sets(client: Client, message: Message):
    args = get_args(message)
    
    try:args[0]
    except:
        await message.edit(settings.get(), disable_web_page_preview=True)
    else:
        cmd_found = settings.get_by_name(args[0])
        
        try:args[1]
        except:pass
        else:
            if args[1] == 'reset':
                cmd_found.set_default_value()
                await warn(message, f'Setting {cmd_found.get_name()} to default value', 'done')
                return

        if cmd_found == None:
            await warn(message, 'Setting not found!')

        else:
            await message.edit(f'<code>{cmd_found}</code> - <b>{cmd_found.get_long_description()}</b>\n<b>Current value:</b> <code>{cmd_found.get_value()}</code>\n<b>Default value: </b><code>{cmd_found.get_default_value()}</code>')

help_menu.add_command('sets', 'Get settings', 'Get list of settings', f'<code>{prefix.get()}sets</code> <code><u>(setting)</u></code> <code>reset</code> <b></i>- for reset setting to default value</i></b>')