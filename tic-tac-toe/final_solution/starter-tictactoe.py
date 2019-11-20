# -*- coding: utf-8 -*-

import time
import Tictactoe 
from random import randint,choice

def RandomMove(b):
    '''Return a random move from the list of possible moves'''
    return b.legal_moves()

def deroulementRandom(b):
    '''Play the Tic-Tac-Toe game randomly.'''
    print("----------")
    print(b)
    if b.is_game_over():
        res = getresult(b)
        if res == 1:
            print("Victory of X")
        elif res == -1:
            print("Victory of O")
        else:
            print("Draw")
        return
    RandomMove(b)
    deroulementRandom(b)


def getresult(b):
    '''Function to evaluate the victory (or not) as X. Return 1 for victory, 0  
       for draw and -1 for lose. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0


board = Tictactoe.Board()
print(board)

### RandomGame
deroulementRandom(board)

print("After the match, every move is undone (thanks to pop()): we get back to the initial board :")
print(board)

