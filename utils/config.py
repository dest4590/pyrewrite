import yaml

class Cfg(dict):
    def __setitem__(self, key, value, default = False):
        super().__setitem__(key, value)
        Config.write(self)
        Config.read(self)

        return value

    def __getitem__(self, key):
        try:
            if isinstance(key, str):
                return super().__getitem__(key)
            elif isinstance(key, tuple):
                return super().__getitem__(key[0])
        except KeyError:
            if isinstance(key, tuple):
                return self.__setitem__(key[0], key[1])
            
    def get(self):
        return dict(self)


class Config:
    sets = Cfg({
        'api_id': '',
        'api_hash': '',
        'debug': False
    })

    def write(sets: Cfg):
        with open('config.yaml', 'w') as file:
            return yaml.dump(sets.get(), file)
        
    def read(self):
        with open('config.yaml', 'r') as file:
            self.sets = Cfg(yaml.load(file, Loader=yaml.FullLoader))
            
    def createSettings(self):
        with open('config.yaml', 'w') as file:
            return yaml.dump(self.sets.get(), file)

cfg = Config()