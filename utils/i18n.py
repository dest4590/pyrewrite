import os as __os__
import yaml as __yaml__
from utils.config import cfg

class I18n_Dict(dict):
    """Dict with locales"""

    def __getitem__(self, key: str):
        print('get: ' + key)
        return super().__getitem__(key)

class Locale:
    """Locale class"""

    def __init__(self):
        print('[Locale] i18n init')
        self.get = I18n_Dict()
        
        # Load locales
        
        self.locale = cfg.sets['lang', 'en']
        
        self.__load_i18n()
    

    def __load_i18n(self):
        """Load `locales.yaml` and fill i18n dict"""

        print('[Locale] Loading locales')

        if __os__.path.exists('locales.yaml'):
            with open('locales.yaml', 'r', encoding='utf-8') as file:
                try: 
                    self.get = __yaml__.load(file, Loader=__yaml__.FullLoader)[self.locale]
                except KeyError:
                    print('[Locale] i18n load error!')
                return self.get
        else:
            return Exception('Please sure you have locales.yaml file!')

i18n = Locale()