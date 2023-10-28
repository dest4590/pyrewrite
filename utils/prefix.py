from utils.config import cfg

class Prefix:
    """Prefix System, use prefix.symbol"""

    cfg.read()

    def __init__(self) -> None:
        print('Prefix init')
        self.symbol = cfg.sets['prefix', '.']

    def __str__(self) -> str:
        return self.symbol

    def set(self, new):
        cfg.sets['prefix'] = new

prefix = Prefix()