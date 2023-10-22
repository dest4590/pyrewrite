from utils.config import cfg
from utils.prefix import prefix

class Setting:
    def __init__(self, name, descShort, descLong, defaultValue) -> None:
        self.name = name
        self.descShort = descShort
        self.descLong = descLong
        self.defaultValue = defaultValue

    def getName(self):
        return self.name

    def getLongDesc(self):
        return self.descLong
    
    def getShortDesc(self):
        return self.descShort
    
    def __str__(self):
        return self.name
    
    def getValue(self):
        return cfg.sets[self.name]

    def getDefaultValue(self):
        return self.defaultValue
    
    def setDefaultValue(self):
        cfg.sets[self.name] = self.defaultValue
    
class Settings:
    settings_dict = {}
    def __init__(self) -> None:
        pass

    def add(self, name, descShort, descLong = None, defaultValue = False):
        """Add setting"""
        try:
            cfg.sets[name, defaultValue]
        except Exception:
            if name != 'prefix':
                cfg[name, defaultValue] = defaultValue

        if descLong is None:
            descLong = descShort

        self.settings_dict[name] = Setting(name, descShort, descLong, defaultValue)

    def get(self):
        """Get settings menu text"""
        settings_text = '<b>Настройки PyRewrite</b>\n'
        for set in self.settings_dict.values():
            setting_name = set.getName()
            set_descShort = set.getLongDesc()
            
            settings_text += f'<code>{setting_name}</code> <b>- {set_descShort}</b>\n'

        return settings_text
    
    def getRaw(self):
        """Get all settings in dict"""
        return [set for set in self.settings_dict.values()]

    def getLen(self):
        """Get settings lenght"""
        return len(self.settings_dict.items())

    def getByName(self, query):
        """Get setting class by name"""
        for set in self.settings_dict.values():
            if set.getName() == query:
                return set
        
        return None
    
    def getValue(self, set_name):
        "Get value of the setting"
        set = self.getByName(set_name)
        return set.getValue()
    
settings = Settings()

# Add settings
settings.add('prefix', 'префикс', 'Меняет префикс юсербота')
settings.add('banner', f'{prefix}info banner', f'меняет баннер {prefix}info команды', 'https://envs.sh/hkf.mp4')
settings.add('info', f'меняет вывод команды {prefix}info', f'Меняет вывод команды {prefix}info menu (может быть full либо lite)', defaultValue='full')