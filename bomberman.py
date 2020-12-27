from person import Person
from colorama import Fore, Back, Style


class Bomberman(Person):

    def __init__(self, _xPos, _yPos):
        Person.__init__(self, _xPos, _yPos)
        self.type = "Bomberman"
        self.score = 0
        self.lives = 2
        self.rep = 'BBBB\nBBBB'
        self.style = Back.GREEN + Fore.BLACK

    def getXpos(self):
        return self._xPos

    def setXpos(self, xPos):
        self._xPos = xPos

    def getYpos(self):
        return self._yPos

    def setXpos(self, yPos):
        self._yPos = yPos

    def rePosition(self):
        self._xPos = 1
        self._yPos = 1

    def increaseLives(self):
        self.lives += 1

    def __repr__(self):
        return self.rep
