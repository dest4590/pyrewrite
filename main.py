from configparser import ConfigParser
from utils.config import *
import os, sys
import logging
import pip
import sys

os.chdir(sys.path[0])

requirements = [
    'install',
    'pyrogram==2.0.104',
    'distro',
    '--upgrade'
]

logging.basicConfig(level=logging.INFO, format='%(message)s')

if not os.path.isfile('config.ini'): # if config doesn't exist
    with open('config.ini', 'w') as cfg:cfg.write('[main]') # create config
    config = ConfigParser()
    config.read('config.ini')
    config.set('main', 'api_id', 'ENTER_YOUR_API_ID')
    config.set('main', 'api_hash', 'ENTER_YOUR_API_HASH')
    config.set('main', 'prefix', '.')
    config.add_section('settings')

    with open('config.ini', 'w') as cfg:config.write(cfg)

    print('Created config!')

read_config()

if get_setting('debug', if_option_not_exist='false') == 'true':
    pip.main(requirements)

from pyrogram import Client

if get_setting('api_id') == 'ENTER_YOUR_API_ID' or get_setting('api_hash') == 'ENTER_YOUR_API_HASH' or get_setting('api_id') == '' or get_setting('api_hash') == '':
    new_api_id = input('Please enter your api_id: ')
    set_setting('api_id', new_api_id)

    new_api_hash = input('Please enter your api_hash: ')
    set_setting('api_hash', new_api_hash)

if not os.path.isdir('plugins/custom/'):
    os.mkdir('plugins/custom/')
    
client = Client(
    'pyrewrite',
    api_id=get_setting('api_id'),
    api_hash=get_setting('api_hash'),
    device_model='PyRewrite',
    plugins = dict(root='plugins'),
)

try:sys.argv[1]
except IndexError:pass
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