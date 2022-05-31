import Node
import MineralNodes
from Player import Player
import random

def printBoard(board):
    for x in range(len(board)):
        print(board[x])
    
    print()

player = Player()

board = [['_' for x in range(10)] for y in range(10)]

minerals = MineralNodes.generateNodes()

for x in range(len(minerals)):
    val = minerals[x].get_value()
    i, j = minerals[x].get_coordinates()

    if val == 10:
        board[i][j] = 'C'
    elif val == 50:
        board[i][j] = 'S'
    else:
        board[i][j] = 'G'


px, py = player.get_coordinates()
board[px][py] = 'P'
moves = 0

while (player.score < 650):
    print("Player score: {}".format(player.score))
    print("Moves: {}".format(moves))
    printBoard(board)

    px, py = player.get_coordinates()
    board[px][py] = "_"
    move = random.randrange(4)
    if move == 0:
        player.moveDown()
    elif move == 1:
        player.moveUp()
    elif move == 2:
        player.moveLeft()
    else:
        player.moveRight()
    pxn, pxy = player.get_coordinates()

    if board[pxn][pxy] != "_":
        player.score += 75
    board[pxn][pxy] = 'P'
    moves += 1

print("Player score: {}".format(player.score))
print("Moves: {}".format(moves))
printBoard(board)


    