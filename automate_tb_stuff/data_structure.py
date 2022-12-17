# Using a data structure to build a tic-tac-toe board.

import pprint

## ======================================================
# Data structure
## ======================================================
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'bottom-L': ' ', 'bottom-M': ' ', 'bottom-R':' '}

pprint.pprint(theBoard)
print(" ")


theBoard['mid-M'] = 'X'

pprint.pprint(theBoard)
print(" ")

## ======================================================
# Function to display data in graphical representation (model) ###
## ======================================================
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['bottom-L'] + '|' + board['bottom-M'] + '|' + board['bottom-R'])

printBoard(theBoard)
print(" ")
