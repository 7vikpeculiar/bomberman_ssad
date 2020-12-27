from person import Person
from air import Air
import random
from colorama import Fore, Back, Style


class Enemy(Person):

    def __init__(self, _xPos, _yPos):
        Person.__init__(self, _xPos, _yPos)
        self.type = "Enemy"
        self.rep = '[^^]\n ][ '
        self.style = Back.GREEN + Fore.RED

    def __repr__(self):
        return self.rep

    def getXpos(self):
        return self._xPos

    def setXpos(self, xPos):
        self._xPos = xPos

    def getYpos(self):
        return self._yPos

    def setXpos(self, yPos):
        self._yPos = yPos

    # Moves the randomly by selecting one of the possible movements
    # that the enemy can make
    def random_move(self, board):
        moves = ['w', 'a', 's', 'd']
        random.shuffle(moves)

        for move in moves:
            if(self.can_move(board, move) > 0):
                self.move(board, move, Air())
                break
