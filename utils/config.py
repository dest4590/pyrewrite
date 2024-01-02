import os

try:
    import yaml
except ModuleNotFoundError:
    os.system('pip install pyyaml')

    from utils.helpers import raw_restart
    print('Restarting')
    raw_restart() # Restart userbot to import libraries

# Using this, because sort_keys=False not working, try it self
yaml.add_representer(dict, lambda self, data: yaml.representer.SafeRepresenter.represent_dict(self, data.items()))

class Cfg(dict):
    "Custom dictionary for config system"

    def __setitem__(self, key, value, default = False):
        super().__setitem__(key, value)
        Config.write(self)
        Config.read(self)
        
        return value

    def __getitem__(self, key):
        try:
            if isinstance(key, str):
                return super().__getitem__(key)
            
            return super().__getitem__(key[0])
        except KeyError:
            if isinstance(key, tuple):
                return self.__setitem__(key[0], key[1])
            
        return None
            
    def get(self):
        return dict(self)


class Config:
    """Simple config system, using `YAML`"""

    def __init__(self):
        print('[PConfig] Config system init')

    sets = Cfg({
        'api_id': '',
        'api_hash': '',
        'debug': False
    })

    def write(sets: Cfg):
        with open('config.yaml', 'w', encoding='utf-8') as file:
            return yaml.dump(sets.get(), file, sort_keys=False)
        
    def read(self):
        with open('config.yaml', 'r', encoding='utf-8') as file:
            self.sets = Cfg(yaml.load(file, Loader=yaml.FullLoader))
            
    def create_settings(self):
        with open('config.yaml', 'w', encoding='utf-8') as file:
            return yaml.dump(self.sets.get(), file)

cfg = Config()