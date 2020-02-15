import numpy as np

#building a suduko board
suduko = np.array([[None, None, None, 7, None, None, 4, None, 1], 
[None, None, 6, None, None, None, None, 3, 2],
[None, 4, None, None, 9, 8, 6, None, None],
[6, None, None, None, None, 4, 8, None, 5],
[1, None, None, None, 6, None, None, None, 9],
[5, None, 8, 9, None, None, None, None, 6],
[None, None, 7, 4, 3, None, None, 1, None],
[8, 1, None, None, None, None, 2, None, None],
[4, None, 2, None, None, 9, None, None, None]])

print(suduko)

#function to check all rows
def checkRow(row):
  for x in range(0,9):
    for y in range (0,9):
      if (x != y):
        if (suduko[x] == suduko[y]):
          print(suduko[x])
          print(suduko[y])
          break
  print(True)

#function to check all cols
def checkCol(colNum):
  for x in range(0,9):
    for y in range(0,9):
      print(x)

#function to check each square
def checkSquare():


checkRow(s)
