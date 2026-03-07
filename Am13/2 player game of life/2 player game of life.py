import turtle
import time


grid = []
with open("player1.in","r") as f: #player 1 (numss)
    nums = f.readlines()
    numss =  [line.strip() for line in nums]
    print(numss)


with open("player2.in","r") as f: #player 2 (numsss)
    nums = f.readlines()
    numsss =  [line.strip() for line in nums]
    print(numsss)



for i in range(10):
    row = []
    for i in range(10):
        row.append(3)
    grid.append(row)
for line in numss: # a loop
    row, collum = line.split()   # "11 31" → "11", "31"
    row = int(row) #int of 11
    collum = int(collum) #int of 31
    grid[row][collum] = 1  #sets it to true

for line in numsss: # a loop
    row, collum = line.split()   # "11 31" → "11", "31"
    row = int(row) #int of 11
    collum = int(collum) #int of 31
    grid[row][collum] = 2 #sets it to true


def printboard(grid):
    print("  0 1 2 3 4 5 6 7 8 9")
    num = 0


    for line in grid:
        print(  num, end=" ")
        num +=1
        for thing in line:
            if thing == 3:
                print("-", end=" ")
            elif thing == 2:
                print("x", end=" ")
            else:
                print("0", end=" ")

        print()

def alive_ded(grid,row,collum,alive):
    # Directions for all 8 neighbors:
    
    live_neighbors = 0
    p1_neighbors = 0
    p2_neighbors = 0
    if row - 1 >= 0 and collum - 1 >= 0 and grid[row - 1][collum -1]== 1:#to p left
        p1_neighbors += 1
        live_neighbors +=1
    if row - 1 >= 0 and collum - 1 >= 0 and grid[row - 1][collum - 1] == 2:
        p2_neighbors += 1
        live_neighbors += 1

    if row - 1 >= 0 and collum + 1 < 10  and grid[row - 1][collum +1] == 1 :#top right
        p1_neighbors += 1
        live_neighbors += 1
    if row - 1 >= 0 and collum + 1 < 10  and grid[row - 1][collum +1] == 2:#top right
        p2_neighbors += 1
        live_neighbors += 1


    if row + 1 < 10 and collum - 1 >= 0  and grid[row +1][collum -1] == 1:#botoom left
        p1_neighbors += 1
        live_neighbors += 1
    if row + 1 < 10 and collum - 1 >= 0  and grid[row +1][collum -1] == 2:#botoom left
        p2_neighbors += 1
        live_neighbors += 1


    if row + 1 < 10 and collum +1 < 10  and grid[row +1][collum +1] == 1:#botoom right
        p1_neighbors += 1
        live_neighbors += 1
    if row + 1 < 10 and collum +1 < 10  and grid[row +1][collum +1] == 2:#botoom right
        p2_neighbors += 1
        live_neighbors += 1


    if collum -1 >= 0  and grid[row][collum - 1] == 1:#left
        p1_neighbors += 1
        live_neighbors += 1
    if collum -1 >= 0  and grid[row][collum - 1] == 2:#left
        p2_neighbors += 1
        live_neighbors += 1


    if collum +1 < 10  and grid[row][collum + 1] == 1:#right
        p1_neighbors += 1
        live_neighbors += 1
    if collum +1 < 10  and grid[row][collum + 1] == 2:#right
        p2_neighbors += 1
        live_neighbors += 1


    if row -1 >= 0 and grid[row - 1][collum] == 1: #top
        p1_neighbors += 1
        live_neighbors += 1
    if row -1 >= 0 and grid[row - 1][collum] == 2: #top
        p2_neighbors += 1
        live_neighbors += 1

    if row + 1 < 10 and grid[row + 1][collum] == 1:
        p1_neighbors += 1
        live_neighbors += 1
    if row + 1 < 10 and grid[row + 1][collum] == 2:
        p2_neighbors += 1
        live_neighbors += 1


    if alive == 1 or alive == 2:
        if live_neighbors <= 1:
            return 3
        if live_neighbors >= 4:
            return 3
        if live_neighbors == 2 or live_neighbors == 3:
            return alive
    else:
        if live_neighbors == 3 and p1_neighbors > p2_neighbors:
            return 1
        elif live_neighbors == 3 and p2_neighbors >p1_neighbors:
            return 2

    return alive

alive_ded(grid,1,1,3)


def player_turn(grid, player):  # Function that handles one player's move
    print(f"\nPlayer {player}'s turn")  # Show whose turn it is

    action = input("Type 'a' to add a cell or 'r' to remove a cell: ").lower()
    # Ask player if they want to add or remove a cell

    while action != "a" and action != "r":
        print("Invalid action")
        action = input("Type 'a' to add a cell or 'r' to remove a cell: ").lower()
    row = int(input("Row (0-9): "))  # Ask for row number
    collum = int(input("Column (0-9): "))  # Ask for column number

    # Check if the position is inside the 10x10 grid
    if 0 <= row < 10 and 0 <= collum < 10:

        if action == "a":  # If player chose to add
            grid[row][collum] = player  # Place their cell (1 or 2)

        elif action == "r":  # If player chose to remove
            grid[row][collum] = 3  # Set the cell to empty

        else:
            print("Invalid action.")  # If they typed something wrong
    else:
        print("Invalid position.")  # If row/column is out of range

    return grid  # Return the updated grid

def player_counter(grid):
    #o = 1
    #x = 2
    p1x = 0
    p20 = 0
    for line in grid:
        for thing in line:
            if thing == 1:
                p20 += 1
            elif thing == 2:
                p1x += 1
    return p1x,p20
                

while True:
    p1 = 0
    p2 = 0

    printboard(grid)  # Print the current grid
    print(f'player 1 has {player_counter(grid)[1]} cells player 2 has {player_counter(grid)[0]} cells')
    if player_counter(grid)[1] == 0:
        print(f'player 2 wins,game over')
        break
    elif player_counter(grid)[0] == 0:
        print(f'player 1 wins,game over')
        break

    # -------------------
    # PLAYER 1 TURN
    # -------------------
    grid = player_turn(grid, 1)  # Let Player 1 make a move


    printboard(grid)  # Show updated grid

    # -------------------
    # PLAYER 2 TURN
    # -------------------
    grid = player_turn(grid, 2)  # Let Player 2 make a move

    printboard(grid)  # Show updated grid

    pcgrid = []
    # pcgrid will store the NEXT generation of the board.
    for i in range(10):
        # This loop creates each row of the new grid.
        row = []
        for j in range(10):
            row.append(False)
        pcgrid.append(row)

    for row in range(10):
        # Loop through every row in the grid.
        for collum in range(10):
            pcgrid[row][collum] = alive_ded(
                grid,  # the CURRENT generation grid
                row,  # row index of the cell
                collum,  # column index of the cell
                grid[row][collum]  # whether the cell is currently alive
            )
    count =+ 1

    grid = pcgrid
