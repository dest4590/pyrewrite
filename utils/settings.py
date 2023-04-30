from utils.config import set_setting, get_setting
from utils.prefix import prefix

class Setting:
    def __init__(self, name, description_short, description_long, default_value) -> None:
        self.name = name
        self.description_short = description_short
        self.description_long = description_long
        self.default_value = default_value

    def get_name(self):
        return self.name

    def get_long_description(self):
        return self.description_long
    
    def get_short_description(self):
        return self.description_short
    
    def __str__(self):
        return self.name
    
    def get_value(self):
        return get_setting(self.name, 'settings')

    def get_default_value(self):
        return self.default_value
    
    def set_default_value(self):
        return set_setting(self.name, self.default_value, 'settings')
    
class Settings:
    settings_dict = {}
    def __init__(self) -> None:
        pass

    def add(self, name, description_short, description_long = None, default_value = '.'):
        try:get_setting(name, 'settings')
        except Exception as e:
            if name != 'prefix':
                set_setting(name, default_value,'settings')

        if description_long == None:
            description_long = description_short

        self.settings_dict[name] = Setting(name, description_short, description_long, default_value)

    def get(self):
        settings_text = '<b>PyRewrite Settings</b>\n'
        for set in self.settings_dict.values():
            setting_name = set.get_name()
            set_description_short = set.get_short_description()
            
            settings_text += f'<code>{setting_name}</code> <b>- {set_description_short}</b>\n'

        return settings_text
    
    def get_raw(self):
        return [set for set in self.settings_dict.values()]

    def get_lenght(self):
        return len(self.settings_dict.items())

    def get_by_name(self, query):
        for set in self.settings_dict.values():
            if set.get_name() == query:
                return set
        
        return None
    
    def get_value(self, set_name, new_value):
        set = self.get_by_name(set_name)
        return set.get_value()
    
settings = Settings()
# Add settings
settings.add('prefix', 'userbot prefix', 'Changes the userbot prefix')
settings.add('banner', f'{prefix.get()}info banner', f'changes {prefix.get()}info banner', 'https://envs.sh/hkf.mp4')