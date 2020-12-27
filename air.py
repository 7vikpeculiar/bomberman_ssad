from colorama import Fore, Back, Style


class Air:

    def __init__(self):
        self.type = "Air"
        self.rep = '    \n    '
        self.style = Back.GREEN

    def __repr__(self):
        return self.rep
