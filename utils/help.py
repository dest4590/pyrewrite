from utils.prefix import prefix
import os

class Command:
    def __init__(self, name, descShort, descLong, usage) -> None:
        self.name = name
        self.descShort = descShort
        self.descLong = descLong
        self.usage = usage

    def getName(self):
        return self.name

    def getLongDesc(self):
        return self.descLong
    
    def getShortDesc(self):
        return self.descShort
    
    def getUsage(self):
        return self.usage

    def __str__(self):
        return self.name
    
class Help_Menu:
    commands = {}

    def __init__(self) -> None:
        pass

    def command(self, name, descShort = 'simple command', descLong = None, usage = 'Not set'):
        if descLong is None:
            descLong = descShort

        self.commands[name] = [name, Command(name, descShort, descLong, usage)]

    def get(self):
        help_text = '<b>Модули PyRewrite</b>\n'

        for command in self.commands.values():
            command_name = command[0]
            command_descShort = command[1].getShortDesc()

            help_text += f'<code>{prefix}{command_name}</code><b> - {str(command_descShort).capitalize()}</b>\n'''
            
 
        return help_text
        
    def getLen(self):
        return len(self.commands.items())
    
    def getByName(self, query):
        for command in self.commands.values():
            if command[1].getName() == query:
                return command[1]
        
        return None
    
    def getLenBuildin(self):
        return len([m for m in os.listdir('plugins') if m not in ['custom', '__pycache__', 'helpers.py']])

    def getLenCustom(self):
        return len([m for m in os.listdir('plugins/custom') if m not in ['__pycache__']])

help_menu = Help_Menu()