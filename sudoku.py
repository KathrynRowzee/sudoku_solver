import os
import sys
from timeit import default_timer as timer
import math

sys.setrecursionlimit(10**8)

initialBoard =  [[0, 1, 8, 0, 0, 2, 3, 0, 4],
                 [0, 0, 3, 5, 0, 0, 0, 0, 0],
                 [5, 2, 4, 8, 9, 0, 0, 0, 0],
                 [1, 0, 5, 0, 7, 0, 4, 0, 6],
                 [0, 0, 7, 0, 0, 0, 9, 0, 0],
                 [2, 0, 9, 0, 4, 0, 5, 0, 8],
                 [0, 0, 0, 0, 8, 9, 6, 4, 3],
                 [0, 0, 0, 0, 0, 7, 2, 0, 0],
                 [0, 0, 1, 6, 0, 0, 7, 8, 0]]

startTime= timer()

def copyBoard(board):
  newBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

  for x in range(9):
    for y in range(9):
      newBoard[x][y] = board[x][y]
  
  return newBoard

def checkRow(board, x, y):
  for rep in range(9):
    if board[x][y] == board[x][rep] and rep != y and board[x][y] != 0:
      return False;
  return True;

def checkCol(board, x, y):
  for rep in range(9):
    if board[x][y] == board[rep][y] and rep != x and board[x][y] != 0:
      return False;
  return True;

def checkBox(board, x, y):
  box = [math.floor(x/3), math.floor(y/3)]

  for rep1 in range(box[0] * 3, box[0] * 3 + 3):
    for rep2 in range(box[1] * 3, box[1] * 3 + 3):
      if board[x][y] == board[rep1][rep2] and x != rep1 and y != rep2:
        return False;

  return True;

def checkWholeBoard(board):
  for x in range(9):
    for y in range(9):
      check = checkRow(board, x, y) and checkCol(board, x, y) and checkBox(board, x, y)
      if(check == False): 
        printBoard(board)
        print('Board is incorrect. Please try again...')
        exit()
        return
  printBoard(board)
  print('Board is correct! Computation successful.')
  exit()

def getTimeElapsed():
  currentTime = timer()
  elapsed = currentTime - startTime
  mins = math.floor(elapsed/60)
  secs = math.floor(elapsed%60)
  if (mins < 10):
    mins = f'0{mins}'
  if (secs < 10):
    secs = f'0{secs}'
  return(f'{mins}:{secs}')

def printBoard(board):
  os.system('clear')
  hBorder = '---------------------'
  print()
  print(hBorder)
  for x in range(9):
    for y in range(9):
      if(board[x][y] < 1 or board[x][y] > 9):
        print(' ', end=' ')
      else:
        print(board[x][y], end=' ')
      if(y == 2 or y == 5):
        print('|', end=' ')
    print()
    if x == 2 or x == 5:
      print(hBorder)
  print(hBorder)
  print(f'Time: {getTimeElapsed()}')

def nextPos(board, x, y, dir):
  if(x == 8 and y == 8 and dir == 1): 
    print('Computation over. Checking work...')
    checkWholeBoard(board)
    return
  if(x == 0 and y == 0 and dir == -1): 
    return

  newX = x
  newY = y + dir

  if(newY == 9):
    newY = 0
    newX = x + 1

  if(newY == -1):
    newY = 8
    newX = x - 1

  if(initialBoard[newX][newY] != 0):
    nextPos(board, newX, newY, dir)
  else:
    printBoard(board)
    incrementAndCheck(board, newX, newY)
      
def incrementAndCheck(board, x, y):
  board[x][y] = board[x][y] + 1

  printBoard(board)

  if (board[x][y] > 9):
    board[x][y] = 0
    nextPos(board, x, y, -1)
  else:
    check = checkRow(board, x, y) and checkCol(board, x, y) and checkBox(board, x, y)

    if (check):
      nextPos(board, x, y, 1)
    else:
      incrementAndCheck(board, x, y)

def solve(board):
  newBoard = copyBoard(board)

  if(newBoard[0][0] != 0):
    nextPos(newBoard, 0, 0, 1)
  else:
    incrementAndCheck(newBoard, 0, 0)

solve(initialBoard)
