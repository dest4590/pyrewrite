import os

from utils.prefix import prefix

class Command:
    "Command for Help_Menu"

    def __init__(self, name, desc_short, desc_long, usage) -> None:
        self.name = name
        self.desc_short = desc_short
        self.desc_long = desc_long
        self.usage = usage

    def get_name(self):
        return self.name

    def get_long_desc(self):
        return self.desc_long
    
    def get_short_desc(self):
        return self.desc_short
    
    def get_usage(self):
        return self.usage

    def __str__(self):
        return self.name
    
class Help_Menu:
    """Help menu"""

    commands = {}

    def __init__(self) -> None:
        pass

    def command(self, name, desc_short = 'simple command', desc_long = None, usage = 'Not set'):
        if desc_long is None:
            desc_long = desc_short

        self.commands[name] = [name, Command(name, desc_short, desc_long, usage)]

    def get(self):
        help_text = '<b>Модули PyRewrite</b>\n'

        for command in self.commands.values():
            command_name = command[0]
            command_desc_short = command[1].get_short_desc()

            help_text += f'<code>{prefix}{command_name}</code><b> - {str(command_desc_short).capitalize()}</b>\n'''
            
 
        return help_text
        
    def get_len(self):
        return len(self.commands.items())
    
    def get_by_name(self, query):
        for command in self.commands.values():
            if command[1].get_name() == query:
                return command[1]
        
        return None
    
    def get_len_buildin(self):
        return len([m for m in os.listdir('plugins') if m not in ['custom', '__pycache__', 'helpers.py']])

    def get_len_custom(self):
        return len([m for m in os.listdir('plugins/custom') if m not in ['__pycache__']])

help_menu = Help_Menu()