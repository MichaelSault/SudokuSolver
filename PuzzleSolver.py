import numpy as np

#building a suduko board
suduko = np.array([
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None]])

correct = np.array([
  [3, 9, 5, 7, 2, 6, 4, 8, 1], 
  [7, 8, 6, 5, 4, 1, 9, 3, 2],
  [2, 4, 1, 3, 9, 8, 6, 5, 7],
  [6, 3, 9, 2, 1, 4, 8, 7, 5],
  [1, 7, 4, 8, 6, 5, 3, 2, 9],
  [5, 2, 8, 9, 7, 3, 1, 4, 6],
  [9, 6, 7, 4, 3, 2, 5, 1, 8],
  [8, 1, 3, 6, 5, 7, 2, 9, 4],
  [4, 5, 2, 1, 8, 9, 7, 6, 3]])

incorrect = np.array([
  [2, 9, 5, 7, 2, 9, 4, 8, 1], 
  [7, 8, 6, 5, 4, 1, 9, 3, 2],
  [2, 4, 1, 3, 9, 8, 2, 5, 7],
  [6, 3, 9, 2, 1, 4, 8, 7, 5],
  [1, 7, 4, 4, 6, 5, 3, 2, 9],
  [5, 2, 8, 9, 7, 3, 1, 4, 6],
  [9, 6, 7, 4, 3, 2, 5, 1, 8],
  [8, 1, 3, 6, 5, 7, 2, 9, 4],
  [4, 5, 2, 1, 8, 9, 7, 1, 3]])

limitsRow = np.array([
  ['<', '<', None, '>', None, None, None, None], 
  ['>', '>', None, None, None, None, None, '<'],
  [None, '<', None, '>', None, None, None, '<'],
  [None, None, None, None, '<', None, '<', '>'],
  ['>', None, None, None, '>', None, None, '<'],
  [None, None, None, '<', None, None, None, None],
  ['<', '<', None, None, None, None, '<', '<'],
  ['<', '<', None, None, '>', None, None, None],
  [None, None, None, None, None, None, '>', '>']])

limitsCol = np.array([
  [None, '^', None, '^', None, 'v', '^', None, '^'], 
  ['v', None, 'v', 'v', None, 'v', None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, 'v', None, 'v', 'v', None, 'v'],
  [None, 'v', 'v', '^', None, None, '^', '^', '^'],
  [None, None, None, None, None, None, None, None, None],
  [None, 'v', 'v', '^', None, None, None, '^', '^'],
  ['v', '^', None, None, '^', '^', None, 'v', None]])

##################################################################
###########CODE TO CHECK IF THE SOLUTION IS VALID#################
##################################################################
#detects errors in row logic
def checkRows(array):
  for x in range(0,9):
    for y in range (0,9):
      for z in range (0,9):
        if (y != z):
          if (array[x][y] == array[x][z]):
            print(x,y)
            print(x,z)
            print("error")
            return False
  print("Finished Rows!")
  return True

#detects errors in col logic
def checkCols(array):
  for x in range(0,9):
    for y in range(0,9):
      for z in range(0,9):
        if (y != z):
          if (array[y][x] == array[z][x]):
            print(y, x)
            print(z, x)
            print("error")
            return False
  print("Finished Cols!")
  return True

#detects errors in square logic
def checkSquares(array):
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      for x in range(0, 3):
        for y in range(0, 3):
          for z in range(0, 3):
            if (y != z):
              if (array[x+i][y+j] == array[x+i][z+j]):
                print(x+i, y+j)
                print(x+i, z+j)
                print("error")
                return False
  print("Finished Squares!")
  return True

# #detects errors in limits
#   for p in range(0,9):
#     for q in range(0,8):
#       if limitsRow[p][q] == '<' :
#         if array[p][q] < array[p][q+1]
#           return True
#       else if limitsRow[p][q] == '>' :
#         if array[p][q] > array[p][q+1]
#           return True
#     return False
  
#   for p in range(0,9):
#     for q in range(0,8):
#       if limitsCol[q][p] == '^' :
#         if array[q][p] < array[q+1][p]
#           return True
#       else if limitsRow[q][p] == 'v' :
#         if array[q+1][p] > array[q+1][p]
#           return True
#     return False


def checkSol(array):
  if checkRows(array):
    if checkCols(array):
      if checkSquares(array):
        print("Your Solution is Valid")
        return True
  print("Your Solution is NOT Valid")
  return False

checkSol(correct)
checkSol(incorrect)


##################################################################
##############CODE TO FIND THE CORRECT SOLUTION###################
##################################################################
def findEmpty(array):
  for x in range(0, 9):
    for y in range(0, 9):
      if (array[x][y] == None):
         return (x, y) #tupple representation of row and col
  return None

def checkValid(array, num, pos):
  #check row
  for m in range(0, 9):
    if array[pos[0]][m] == num and pos[1] != m:
      return False

  #check col
  for m in range(0, 9):
    if array[m][pos[1]] == num and pos[0] != m:
      return False

  #check box
  boxX = pos[1] // 3
  boxY = pos[0] // 3

  for i in range(boxY * 3, boxY * 3 + 3):
    for j in range(boxX * 3, boxX * 3 + 3):
      if array[i][j] == num and (i,j) != pos:
        return False
  
  if pos[1] > 0:
    if limitsRow[pos[0]][pos[1]-1] == '<':
      if array[pos[0]][pos[1]-1] > num:
        return False
    elif limitsRow[pos[0]][pos[1]-1] == '>':
      if array[pos[0]][pos[1]-1] < num:
        return False

  if pos[0] > 0:
    if limitsCol[pos[0]-1][pos[1]] == '^':
      if array[pos[0]-1][pos[1]] > num:
        return False
    elif limitsCol[pos[0]-1][pos[1]] == 'v':
      if array[pos[0]-1][pos[1]] < num:
        return False

  print(suduko)
  print("===========================================================")
  return True

def solver(array):
  find = findEmpty(array)
  if not find:
    return True
  else:
    row, col = find
  
  for i in range(1, 10):
    if checkValid(array, i, (row, col)):
      array[row][col] = i
      if solver(array):
        return True

      array[row][col] = None

  return False


##################################################################
################FANCY PRINT FUNCTION FOR BOARD####################
##################################################################

def printBoard(array):
  print ("-------------------------------")
  for i in range (0,9):
    if i == 3 or i == 6:
      print ("-------------------------------")
    print ("|" , array[i][0:3], "|" , array[i][3:6], "|" , array[i][6:9], "|")
  print ("-------------------------------")
  print ('\n\n')


  #####MAIN FUNCTION#####
  printBoard(suduko)
  solver(suduko)
  printBoard(suduko)
