from colorama import Fore, Back, Style
from explosion import Explosion


class Bomb:

    def __init__(self, _xPos, _yPos):
        self._xPos = _xPos
        self._yPos = _yPos
        self.type = "Bomb"
        self.timer = 2
        self.style = Back.RED + Fore.WHITE
        self.exploded = False

    # Bomb is represented as the time in the timer
    def __repr__(self):
        rep = ''
        if self.timer >= 0:
            for i in range(2):
                for i in range(4):
                    rep = rep + str(self.timer + 1)
                rep = rep + '\n'
        else:
            for i in range(2):
                for i in range(4):
                    rep = rep + str('e')
                rep = rep + ''
        return rep

    # It decrese the time if it greater than 0
    # else return 0
    def decCount(self):
        if(self.timer > 0):
            self.timer = self.timer - 1
            return 1
        else:
            self.timer = -1
            return 0

    # Explode the bomb present in the board
    def explode(self, board, player, bomb):
        curX = self._xPos
        curY = self._yPos

        tag = 1

        for i in [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]:
            if(self.semiExplode(board, player, bomb, curX + i[0], curY + i[1]) == -1):
                tag = -1

        if(player._xPos == curX and player._yPos == curY):
            tag = -1

        self.exploded = True
        return tag

    # Helper function to the explode function
    def semiExplode(self, board, player, bomb, curX, curY):
        if board.board[curX][curY].type in ['Wall', 'Explosion']:
            return 1

        if board.board[curX][curY].type in ['Brick']:
            player.score += 20

        if board.board[curX][curY].type in ['Enemy']:
            player.score += 100

        if board.board[curX][curY].type in ['Bomberman']:
            board.board[curX][curY] = Explosion(curX, curY)
            board.activeExplosions.append(board.board[curX][curY])
            return -1

        board.board[curX][curY] = Explosion(curX, curY)
        board.activeExplosions.append(board.board[curX][curY])
        return 1

    def getXpos(self):
        return self._xPos

    def setXpos(self, xPos):
        self._xPos = xPos

    def getYpos(self):
        return self._yPos

    def setXpos(self, yPos):
        self._yPos = yPos
