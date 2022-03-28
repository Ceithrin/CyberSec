import requests
from bs4 import BeautifulSoup
import math

session = requests.session()

# N is the size of the 2D matrix   N*N
N = 9
 
# A utility function to print grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):
   
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSudoku(grid, row, col):
   
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if (row == N - 1 and col == N):
        return True
       
    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0
 
    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
       
        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(grid, row, col, num):
           
            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            grid[row][col] = num
 
            # Checking for next possibility with next
            # column
            if solveSudoku(grid, row, col + 1):
                return True
 
        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        grid[row][col] = 0
    return False

response = session.get('http://challs.dvc.tf:6002/home?', verify=False)

content = response.content.decode()

# print(content)

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

to_send = []

soup = BeautifulSoup(content, features="html.parser")
inputs = soup.find_all('input', {'disabled': ''})
for input in inputs[:-1]:
    if input.get('value'):
        number = int(input.get('name'))
        value = int(input.get('value'))
        print(number, value)
        if number < 10:
            grid[0][number - 1] = value
        elif number < 19:
            grid[1][number % 10] = value
        elif number < 28:
            grid[2][(number + 1) % 10] = value
        elif number < 37:
            grid[3][(number + 2) % 10] = value
        elif number < 46:
            grid[4][(number + 3) % 10] = value
        elif number < 55:
            grid[5][(number + 4) % 10] = value
        elif number < 64:
            grid[6][(number + 5) % 10] = value
        elif number < 73:
            grid[7][(number + 6) % 10] = value
        elif number < 82:
            grid[8][(number + 7) % 10] = value
    else:
        to_send.append(int(input.get('name')))


printing(grid)
print(to_send)
print()


if (solveSudoku(grid, 0, 0)):
    print(grid)
else:
    print("no solution  exists ")
 
    # This code is contributed by sudhanshgupta2019a


params = {
    "1": 3,
    "2" : 8,
}

a = 1
for i in range(9):
    for j in range(9):
        params[str(a)] = grid[i][j]
        a = a + 1

print(params)

response = session.post('http://challs.dvc.tf:6002/flag', data=params, verify=False)

print(response.content.decode())