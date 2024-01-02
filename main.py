import logging
import os
import sys

logo = '''
  ___        ___                    _  _        
 | _ \ _  _ | _ \ ___ __ __ __ _ _ (_)| |_  ___ 
 |  _/| || ||   // -_)\ V  V /| '_|| ||  _|/ -_)
 |_|   \_, ||_|_\\\\___| \_/\_/ |_|  |_| \\__|\___|
       |__/                                     
'''

print(logo)

try:
    from utils.config import cfg
    from pyrogram import Client
    
    if os.name != 'nt':
        import distro  # pylint: disable=W0611 # noqa: F401
        
except ModuleNotFoundError:
    for module in ['pyrogram', 'distro', 'tgcrypto']:
        print('Installing module: ' + module)
        os.system('pip install ' + module)

    from utils.helpers import raw_restart
    print('Restarting')
    raw_restart() # Restart userbot to import libraries

os.chdir(sys.path[0])

# Configure pyrogram logger
logging.basicConfig(level=logging.INFO, format='%(message)s')

if not os.path.exists('config.yaml'):
    cfg.create_settings()

    print('A config has been created, please fill in all fields in the config and restart the userbot')
    sys.exit(0)

cfg.read()

from utils.i18n import i18n

if cfg.sets['api_id'] == '' or cfg.sets['api_hash'] == '':
    new_api_id = input(i18n.get['enter-api-id'])
    cfg.sets['api_id'] = new_api_id
    
    new_api_hash = input(i18n.get['enter-api-hash'])
    cfg.sets['api_hash'] = new_api_hash

    cfg.write()

if not os.path.isdir('plugins/custom/'):
    os.mkdir('plugins/custom/')
    
client = Client(
    cfg.sets['session', 'pyrewrite'],
    api_id=str(cfg.sets['api_id']),
    api_hash=str(cfg.sets['api_hash']),
    device_model='PyRewrite',
    plugins = {'root': 'plugins'},
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
        client.edit_message_text(int(chat_id), int(message_id), i18n.get['restarted'])

client.run()