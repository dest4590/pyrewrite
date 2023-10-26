from utils.config import cfg
from utils.prefix import prefix

class Setting:
    """Setting for class Settings"""

    def __init__(self, name, desc_short, desc_long, defaultValue) -> None:
        self.name = name
        self.desc_short = desc_short
        self.desc_long = desc_long
        self.defaultValue = defaultValue

    def get_name(self):
        return self.name

    def get_long_desc(self):
        return self.desc_long
    
    def get_short_desc(self):
        return self.desc_short
    
    def __str__(self):
        return self.name
    
    def get_value(self):
        return cfg.sets[self.name]

    def get_default_value(self):
        return self.defaultValue
    
    def set_default_value(self):
        cfg.sets[self.name] = self.defaultValue
    
class Settings:
    """Settings system, use settings_dict to get settings"""

    settings_dict = {}


    def add(self, name, desc_short, desc_long = None, defaultValue = False):
        """Add setting"""
        try:
            cfg.sets[name, defaultValue]
        except Exception:
            if name != 'prefix':
                cfg[name, defaultValue] = defaultValue

        if desc_long is None:
            desc_long = desc_short

        self.settings_dict[name] = Setting(name, desc_short, desc_long, defaultValue)

    def get(self):
        """Get settings menu text"""
        settings_text = '<b>Настройки PyRewrite</b>\n'

        for setting in self.settings_dict.values():
            setting_name = setting.get_name()
            set_desc_short = setting.get_long_desc()
            
            settings_text += f'<code>{setting_name}</code> <b>- {set_desc_short}</b>\n'

        return settings_text
    
    def get_raw(self):
        """Get all settings in dict"""
        return list(self.settings_dict.values())

    def get_len(self):
        """Get settings lenght"""
        return len(self.settings_dict.items())

    def get_by_name(self, query):
        """Get setting class by name"""
        for setting in self.settings_dict.values():
            if setting.get_name() == query:
                return setting
        
        return None
    
    def get_value(self, set_name):
        "Get value of the setting"
        setting = self.get_by_name(set_name)
        return setting.get_value()
    
settings = Settings()

# Add settings
settings.add('prefix', 'префикс', 'Меняет префикс юсербота')
settings.add('banner', f'{prefix}info banner', f'меняет баннер {prefix}info команды', 'https://envs.sh/hkf.mp4')
settings.add('info', f'меняет вывод команды {prefix}info', f'Меняет вывод команды {prefix}info menu (может быть full либо lite)', defaultValue='full')