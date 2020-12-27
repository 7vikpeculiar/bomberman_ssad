from colorama import Fore, Back, Style


class Brick:

    def __init__(self):
        self.type = "Brick"
        self.rep = "////\n////"
        self.style = Back.GREEN + Fore.WHITE

    def __str__(self):
        return self.rep
