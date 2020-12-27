from brick import Brick
from wall import Wall
from air import Air
from bomb import Bomb
from bomberman import Bomberman
from enemy import Enemy
import os
import random
from colorama import Fore, Back, Style


class Board:

    def __init__(self, rows, columns, maxEnemy, maxBrick, player):
        self.rows = rows
        self.columns = columns
        self.maxBrick = maxBrick
        self.maxEnemy = maxEnemy
        self.time = 120
        self.board = []
        self.precentBoxes = 0.1
        self.precentEnemies = 0.1
        self.player = player
        self.enemies = []
        self.bombs = []
        self.activeExplosions = []

        for i in range(rows):
            temp = []
            for j in range(columns):
                temp.append(Air())
            self.board.append(temp)

    # Construct's the Games Board
    def build(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if(i == 0 or i == self.rows - 1 or j == 0 or j == self.columns - 1):
                    self.board[i][j] = Wall()
                elif (i == 1 and j == 1):
                    self.board[i][j] = self.player
                elif (i == 2 and j == 1) or (i == 1 and j == 2):
                    self.board[i][j] = Air()
                elif (i % 2 == 0 and j % 2 == 0):
                    self.board[i][j] = Wall()
                elif random.random() < self.precentBoxes and self.maxBrick > 0:
                    self.maxBrick -= 1
                    self.board[i][j] = Brick()
                elif random.random() < self.precentEnemies and self.maxEnemy > 0:
                    self.maxEnemy -= 1
                    self.board[i][j] = Enemy(i, j)
                    self.enemies.append(self.board[i][j])

    def __repr__(self):
        os.system('clear')
        boardStr = ''
        for i in range(self.rows):
            for j in range(2):
                for k in range(self.columns):
                    boardStr = boardStr + \
                        self.board[i][k].style + str(self.board[i][k]).split('\n')[j] + Style.RESET_ALL
                boardStr = boardStr + '\n'
        return boardStr
