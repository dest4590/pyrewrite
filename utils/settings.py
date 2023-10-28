from utils.config import cfg
from utils.i18n import i18n

class Setting:
    """Setting for class Settings"""

    def __init__(self, name, desc_short, desc_long, default_value) -> None:
        self.name = name
        self.desc_short = desc_short
        self.desc_long = desc_long
        self.default_value = default_value

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
        return self.default_value
    
    def set_default_value(self):
        cfg.sets[self.name] = self.default_value
    
class Settings:
    """Settings system, use settings_dict to get settings"""

    settings_dict = {}


    def add(self, name, desc_short, desc_long = None, default_value = False):
        """Add setting"""
        try:
            cfg.sets[name, default_value]
        except Exception:
            if name != 'prefix':
                cfg[name, default_value] = default_value

        if desc_long is None:
            desc_long = desc_short

        self.settings_dict[name] = Setting(name, desc_short, desc_long, default_value)

    def get(self):
        """Get settings menu text"""
        settings_text = i18n.get['settings-banner']

        for setting in self.settings_dict.values():
            setting_name = setting.get_name()
            set_desc_short = setting.get_long_desc()

            settings_text += i18n.get['setting-in-menu'].format(setting_name, set_desc_short)

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
settings.add('prefix', i18n.get['setting-prefix-short-desc'], i18n.get['setting-prefix-long-desc'])
settings.add('banner', i18n.get['setting-banner-short-desc'], i18n.get['setting-banner-short-desc'], 'https://envs.sh/hkf.mp4')
settings.add('info', i18n.get['setting-info-short-desc'], i18n.get['setting-info-long-desc'], default_value='full')
settings.add('lang', i18n.get['setting-lang-short-desc'], i18n.get['setting-lang-short-desc'], default_value='en')