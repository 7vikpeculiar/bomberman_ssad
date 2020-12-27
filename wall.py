from colorama import Fore, Back, Style


class Wall:

    penetrate = False

    def __init__(self):
        self.type = "Wall"
        self.rep = "XXXX\nXXXX"
        self.style = Back.BLACK + Fore.LIGHTWHITE_EX

    def __str__(self):
        return self.rep
