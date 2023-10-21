from pyrogram import Client, filters
from pyrogram.types import Message
from utils.prefix import prefix
from utils.help import help_menu
from utils.helpers import getArgs, warn
import os
import pyrogram.errors

@Client.on_message(filters.command('terminal', prefixes=prefix.symbol) & filters.me)
async def exm(client: Client, message: Message):
    args = getArgs(message)
    
    await warn(message, 'Executing...', 'time')

    output = os.popen(' '.join(args)).read()
    
    try:
        await warn(message, f'<b>Done:</b>\n<b>Command:\n</b><code>{" ".join(args)}</code> <code>\n' + output + '</code>', 'done', raw=True)

    except pyrogram.errors.exceptions.bad_request_400.MessageTooLong:
        await warn(message, 'Error: Message to long!\nSending as file...')
        
        with open('./output.txt', 'w', encoding='utf-8', errors='ignore') as out:
            out.write(output)
        
        await client.send_document(message.chat.id, './output.txt')
        
        os.remove('./output.txt')

help_menu.command('terminal', 'Terminal output', 'Send you output from terminal')