from pyrogram.types import Message
import random
import os, sys

def get_args(msg: Message):
    return str(msg.text).split(' ')[1:]

async def warn(msg: Message, text: str, type = 'error', raw = False):
    """Warn/Info about command"""

    if type == 'error':
        if not raw:
            await msg.edit(f'❌ <b>{text[0].upper() + text[1:]}</b>')
        elif raw:
            await msg.edit(f'❌ {text[0].upper() + text[1:]}')

    elif type == 'info':
        if not raw:
            await msg.edit(f'ℹ <b>{text[0].upper() + text[1:]}</b>')
        elif raw:
            await msg.edit(f'ℹ {text[0].upper() + text[1:]}')

    elif type == 'time':
        if not raw:
            await msg.edit(f'⏳ <b>{text[0].upper() + text[1:]}</b>')
        elif raw:
            await msg.edit(f'⏳ {text[0].upper() + text[1:]}')

    elif type == 'done':
        if not raw:
            await msg.edit(f'✅ <b>{text[0].upper() + text[1:]}</b>')
        elif raw:
            await msg.edit(f'✅ {text[0].upper() + text[1:]}')
        
    return msg

def text_animation(text):
    symbols = ['*', '@', '#', '$', '%', '^', '&', '&']
    temp = text
    temp += temp[:1]
    shif = []
    for i in range(1, len(temp) + 1):
        shif.append(random.choice(symbols))
    steps = []
    phrase = []
    for i in range(1, int(len(temp)) + 1):
        phrase.append(temp[i - 1:i])
    x = 0
    for i in phrase:
        shif.pop(x)
        str = ''.join(shif)
        steps.append(str)
        shif.insert(x, i)
        str = ''.join(shif)
        x += 1
    return steps

def get_system():
    system = 'Linux 🐧' if os.name == 'posix' else 'Windows 💻'
    if os.name == 'posix':
        if 'termux' in sys.executable.lower():
            system = 'Termux 📱'
        else:
            import distro
            system = distro.name(pretty=False)