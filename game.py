from board import Board
from alarmexception import *
from getchunix import *
from air import Air
from explosion import Explosion
from bomberman import Bomberman
import os
from bomb import Bomb
import time

getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


'''
The "input_to" function return key pressed by user within "timeout" time.
If no input is given within timeout it will return null string
'''


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

# gameOver Function prints the current status of board and quits the game


def gameOver(player):
    os.system('clear')
    print board
    print 'Score :', player.score
    print 'Game Over'
    exit()


'''
movePlayer takes Board Instance and input as arguments and take action
accordingly
'''


def movePlayer(board, inp):
    # If input is 'b' we insert a bomb if no other bomb is active
    # i.e Allow only one active Bomb at a given instant
    if(inp == 'b'):
        if(len(bombs) == 0):
            bombs.append(Bomb(bomberman._xPos, bomberman._yPos))
    # can_move returns -1 if player dies after making the move
    elif(bomberman.can_move(board.board, inp) == -1):
        playerDied(board, bomberman)
    # else player is moved and the current place is replaced by Air()
    else:
        bomberman.move(board.board, inp, Air())


'''
playerDied takes Board Instance and Bomberman Instance
If playerDies dies and no lives are left it will quit the game
Else decrease players lives
'''


def playerDied(board, player):
    if player.lives > 0:
        player.lives -= 1
        print(board)
        print("You Died")

        # Making sure the place where player spans after dieing is free of
        # enemies or Explosion
        if player._xPos == 1 and player._yPos == 1:
            if board.board[player._xPos][player._yPos].type == "Enemy":
                board.enemies.remove(board.board[player._xPos][player._yPos])
            elif board.board[player._xPos][player._yPos].type == "Explosion":
                board.activeExplosions.remove(
                    board.board[player._xPos][player._yPos])
            board.board[player._xPos][player._yPos] = Air()
        # Removing Bomber from board
        if board.board[player._xPos][player._yPos].type == "Bomberman":
            board.board[player._xPos][player._yPos] = Air()
        player.rePosition()
        board.board[1][1] = player
    else:
        gameOver(player)


player = Bomberman(1, 1)

for level in range(1, 4):
    # Initializing Board
    player.rePosition()
    player.increaseLives()
    board = Board(21, 21, 5 * level, 50, player)
    board.build()

    # Stores the List of enemies
    bomberman = board.player
    enemies = board.enemies
    bombs = board.bombs
    endTime = time.time() + board.time
    roundStatus = False

    # Next step is used move enemies after desired time
    nextStep = time.time() + 1

    while time.time() <= endTime:
        # If all enemies dies moving to nex level
        if len(enemies) == 0:
            os.system('clear')
            print('You win')
            print("Next Level")
            roundStatus = True
            time.sleep(0.5)
            break

        inp = input_to()

        if(inp == 'q'):
            gameOver(bomberman)

        movePlayer(board, inp)

        # Show Bomb after player moves after inserting bomb
        for i in range(len(bombs)):
            if board.board[bombs[i]._xPos][bombs[i]._yPos].type == "Air":
                board.board[bombs[i]._xPos][bombs[i]._yPos] = bombs[i]

        if(time.time() >= nextStep):
            nextStep = time.time() + 1

            # Remove the explosion
            for explosion in board.activeExplosions:
                board.board[explosion._xPos][explosion._yPos] = Air()
            board.activeExplosions = []

            # Decrease Timer of bomb and explode if bomb's timer timeout
            tag = 1
            temp = []
            for i in range(len(bombs)):
                if bombs[i].decCount() == 0:
                    if(bombs[i].explode(board, bomberman, bombs[i])) == -1:
                        playerDied(board, bomberman)
                        tag = 0
                else:
                    temp.append(bombs[i])
            bombs = []
            for i in temp:
                bombs.append(i)

            # Remove enemies from list after they die
            for enemy in enemies:
                if board.board[enemy._xPos][enemy._yPos] != enemy:
                    board.enemies.remove(enemy)
            enemies = board.enemies

            # Move Enemy randomly
            for enemy in enemies:
                enemy.random_move(board.board)

        if(board.board[bomberman._xPos][bomberman._yPos] != bomberman):
            playerDied(board, bomberman)
            tag = 0

        # Print the board if the player didn't die
        if tag:
            print board
            print '\t\tLevel : ', level
            print 'Time Left : ', int(endTime - time.time()), '\t Lives Left: ', bomberman.lives
            print 'Score: ', bomberman.score

    # If roundStatus is True we should move to next level
    # Else Quit game as Time's up
    if not roundStatus:
        print("Time Up")
        break
