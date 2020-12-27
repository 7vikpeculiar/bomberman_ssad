from colorama import Fore, Back, Style


class Explosion:

    def __init__(self, _xPos, _yPos):
        self._xPos = _xPos
        self._yPos = _yPos
        self.type = "Explosion"
        self.active = True
        self.style = Back.RED + Fore.WHITE

    def __str__(self):
        return 'eeee\neeee'

    def getXpos(self):
        return self._xPos

    def setXpos(self, xPos):
        self._xPos = xPos

    def getYpos(self):
        return self._yPos

    def setXpos(self, yPos):
        self._yPos = yPos
