from air import Air
from wall import Wall
from brick import Brick


class Person:

    def __init__(self, _xPos, _yPos):
        self._xPos = _xPos
        self._yPos = _yPos

    def getXpos(self):
        return self._xPos

    def setXpos(self, xPos):
        self._xPos = xPos

    def getYpos(self):
        return self._yPos

    def setXpos(self, yPos):
        self._yPos = yPos

    # Checks if given move is possible or not
    # And return -1 if the person dies making given move
    def check_move(self, board, curX, curY):
        if not(board[curX][curY].type in ["Wall", "Brick", "Bomb"]):
            if board[self._xPos][self._yPos].type == "Enemy":
                if board[curX][curY].type == 'Explosion':
                    return 0
                elif board[curX][curY].type != 'Enemy':
                    return 1
                else:
                    return 0
            if board[self._xPos][self._yPos].type == "Bomberman":
                if board[curX][curY].type == 'Enemy' or board[curX][curY].type == 'Explosion':
                    return -1
                else:
                    return 1
        return 0

    def can_move(self, board, move):
        if move == 'w':
            return self.check_move(board, self._xPos - 1, self._yPos)
        elif move == 'a':
            return self.check_move(board, self._xPos, self._yPos - 1)
        elif move == 's':
            return self.check_move(board, self._xPos + 1, self._yPos)
        elif move == 'd':
            return self.check_move(board, self._xPos, self._yPos + 1)
        return 0

    # Moves the person according to given input
    def move(self, board, move, cur):
        if self.can_move(board, move):
            if move == 'w':
                board[self._xPos - 1][self._yPos] = board[self._xPos][self._yPos]
                board[self._xPos][self._yPos] = cur
                self._xPos = self._xPos - 1
                return True
            if move == 'a':
                board[self._xPos][self._yPos -
                                  1] = board[self._xPos][self._yPos]
                board[self._xPos][self._yPos] = cur
                self._yPos = self._yPos - 1
                return True
            if move == 's':
                board[self._xPos + 1][self._yPos] = board[self._xPos][self._yPos]
                board[self._xPos][self._yPos] = cur
                self._xPos = self._xPos + 1
                return True
            if move == 'd':
                board[self._xPos][self._yPos +
                                  1] = board[self._xPos][self._yPos]
                board[self._xPos][self._yPos] = cur
                self._yPos = self._yPos + 1
                return True
