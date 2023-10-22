from utils.config import cfg
import logging
import os
import sys

try:
    from pyrogram import Client
    from loguru import logger
    import distro  # noqa: F401
except ImportError:
    for module in ['loguru', 'pyrogram', 'distro', 'tgcrypto']:
        os.system('pip install ' + module)

    from utils.helpers import RawRestart
    RawRestart() # Restart userbot to import libraries

os.chdir(sys.path[0])

logging.basicConfig(level=logging.INFO, format='%(message)s')

if os.path.exists('config.yaml') is False:
    cfg.createSettings()

    logger.info('Создан конфиг, пожалуйста, заполните все поля в конфиге и перезапустите юсербота')
    sys.exit(0)

cfg.read()

if cfg.sets['api_id'] == '' or cfg.sets['api_hash'] == '':
    new_api_id = input('Пожалуйста введите свой api_id: ')
    cfg.sets['api_id'] = new_api_id
    

    new_api_hash = input('Теперь введите api_hash: ')
    cfg.sets['api_hash'] = new_api_hash

    cfg.write()

if not os.path.isdir('plugins/custom/'):
    os.mkdir('plugins/custom/')
    
client = Client(
    cfg.sets['session', 'pyrewrite'],
    api_id=str(cfg.sets['api_id']),
    api_hash=str(cfg.sets['api_hash']),
    device_model='PyRewrite',
    plugins = dict(root='plugins'),
)

try:
    sys.argv[1]
except IndexError:
    pass
else:
    sys_args = sys.argv[1].split(',')
    message_id = sys_args[0]
    chat_id = sys_args[1]

    with client:
        client.edit_message_text(int(chat_id), int(message_id), '✅ <b>Restarted!</b>')

logo = '''
  ___        ___                    _  _        
 | _ \ _  _ | _ \ ___ __ __ __ _ _ (_)| |_  ___ 
 |  _/| || ||   // -_)\ V  V /| '_|| ||  _|/ -_)
 |_|   \_, ||_|_\\\\___| \_/\_/ |_|  |_| \__|\___|
       |__/                                     
'''
print(logo)

client.run()