# PROJECT FILE

- Bomberman game
  - Played in a grid containing enemies which can be killed using bombs
  - Enemies are able to kill the bomberman when they meet the Bomberman
  - They are 3 levels implemented
  - Each level contains 3 lifes
  - After each level we get an extra life
  - Each level has a time limit of 120 seconds
  - 20 points for brick and 100 points for destroying enemy
  - Each level should be finished within the time given
  - You can be killed by an enemy whenever he approaches You
  - The bomb explodes in 3 second

##Prerequisites
- python
- colorama : pip install colorama
- getch : pip install getch
- os
- sys
- signal
- time
- random

##USAGE
 - In the bomberman directory run the game.py file
 - USAGE : "python game.py"

##Implementation
 - Air,Board,Bomb,Bomberman,Brick,Enemy,Explosion,Person
    classes have been implemented for the game
 - enemy , bomberman inherit person class
 - all the files are linked together in the game.py file

##BONUS IMPLEMENTATION
  - Implemented different colors for the enemies,board,bomberman,explosion,bomb
  - Implemented upto 3 levels of play
  - Implemented the counter for the bomb
