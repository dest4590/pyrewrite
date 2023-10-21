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

    logger.info('Config file is created. Please, fill all fields in config, and restart')
    sys.exit(0)

cfg.read()

if cfg.sets['api_id'] == '' or cfg.sets['api_hash'] == '':
    new_api_id = input('Please enter your api_id: ')
    cfg.sets['api_id'] = new_api_id
    

    new_api_hash = input('Please enter your api_hash: ')
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
  ______   ______  _______        ______  ___ _____ _____ 
 |  _ \ \ / /  _ \| ____\ \      / /  _ \|_ _|_   _| ____|
 | |_) \ V /| |_) |  _|  \ \ /\ / /| |_) || |  | | |  _|  
 |  __/ | | |  _ <| |___  \ V  V / |  _ < | |  | | | |___ 
 |_|    |_| |_| \_\_____|  \_/\_/  |_| \_\___| |_| |_____|
                                                          '''

print(logo)

client.run()