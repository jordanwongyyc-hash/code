
# If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
# If the cell is dead, then it springs to life only in the case that it has 3 live neighbors
# Game of Life Rules
# For a space that is populated:
# Examples
# Each cell with one or no neighbors dies, as if by solitude.
#
#
# Each cell with four or more neighbors dies, as if by overpopulation.
#
#
# Each cell with two or three neighbors survives.
#
#
# For a space that is empty or unpopulated:
#
# Each cell with three neighbors becomes populated.


import turtle
import time



grid = []
with open("hertz-oscillator.in","r") as f:
    nums = f.readlines()
    numss =  [line.strip() for line in nums]
    print(numss)
for i in range(30):
    row = []
    for i in range(60):
        row.append(False)

    grid.append(row)

for line in numss: # a loop
    row, collum = line.split()   # "11 31" → "11", "31"
    row = int(row) #int of 11
    collum = int(collum) #int of 31
    grid[row][collum] = True #sets it to true



def printboard(grid):
    for line in grid:
        for thing in line:
            if thing == False:
                print("-", end="")
            else:
                print("O", end="")
        print()
def alive_ded(grid,row,collum,alive):
    # Directions for all 8 neighbors:
    live_neighbors = 0

    if row - 1 >= 0 and collum - 1 >= 0 and grid[row - 1][collum -1]:#top left
        live_neighbors += 1

    '''directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),        (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]'''
    if row - 1 >= 0 and collum + 1 < 60  and grid[row - 1][collum +1]:#top right
        live_neighbors += 1

    if row + 1 < 30 and collum - 1 >= 0  and grid[row +1][collum -1]:#botoom left
        live_neighbors += 1

    if row + 1 < 30 and collum +1 < 60  and grid[row +1][collum +1]:#botoom right
        live_neighbors += 1

    if collum -1 >= 0  and grid[row][collum - 1]:#left
        live_neighbors += 1

    if collum +1 < 60  and grid[row][collum + 1]:#right
        live_neighbors += 1

    if row -1 >= 0 and grid[row - 1][collum] : #top
        live_neighbors += 1

    if row + 1 < 30 and grid[row + 1][collum]:

        live_neighbors += 1
    if alive:
        if live_neighbors <= 1:
            return False
        if live_neighbors >= 4:
            return False
        if live_neighbors == 2 or live_neighbors == 3:
            return True
    else:
        if live_neighbors == 3:
            return True
        else:
            return alive





'''

alive_ded(grid,12,32,True)'''

printboard(grid)


input()
while True:
    print("\033c")

    pcgrid = []
    # pcgrid will store the NEXT generation of the board.

    for i in range(30):
        # This loop creates each row of the new grid.
        row = []
        for j in range(60):
            row.append(False)
        pcgrid.append(row)

    for row in range(30):
        # Loop through every row in the grid.
        for collum in range(60):
            # Loop through every column in the current row.

               #function calling
            pcgrid[row][collum] = alive_ded(
                grid,                # the CURRENT generation grid
                row,                 # row index of the cell
                collum,              # column index of the cell
                grid[row][collum]    # whether the cell is currently alive
            )

            # It returns:
            # True  -> the cell will be alive next generation
            # False -> the cell will be dead next generation
            # This value is saved into pcgrid.

    grid = pcgrid
    # The new grid (next generation) replaces the old grid.
    # The game has now advanced one full generation.



    printboard(grid)
    time.sleep(0.2)
    # input()


