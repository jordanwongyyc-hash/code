
grid = []
import random

# Build 3x3 grid like your method
for i in range(3):        # 3 rows
    row = []
    for r in range(3):        # 3 columns
        row.append(" ")          # empty cell
    grid.append(row)
def printboard(grid):
    for r in range(3):                                  # loop rows
        for c in range(3):
            if c < 2:
                print(f' {grid[r][c]} |',end = "")
            else:
                print(f' {grid[r][c]} ', end="")

        if r < 2:                                      # avoid extra line at bottom after 3 line
            print("\n---+---+---")            # divider line
    print("\n")


def copy_grid(grid):#for ai
    new_grid = []
    for row in grid:
        new_grid.append(row.copy())  # copies each row
    return new_grid
def win(grid,player):
    for i in range(3):
        if grid[i][0] == player and grid[i][1] == player  and grid[i][2] == player:
            return True
        if grid[0][i] == player and grid[1][i] ==player and grid[2][i] == player:
            return True
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player  and grid[1][1] == player and grid[2][0] == player:
        return True
    else:
        return False
def aipredict(grid):
    new_grid = copy_grid(grid)
    for row in range(3):#win
        for collum in range(3):#win
            if new_grid[row][collum] == " ":
                new_grid[row][collum] = "o"
                result = win(new_grid,"o")
                new_grid = copy_grid(grid)
                if result == True:
                    return [row,collum]

    for row in range(3):#block
        for collum in range(3):
            if new_grid[row][collum] == " ":
                new_grid[row][collum] = "x"
                result = win(new_grid,"x")

                new_grid = copy_grid(grid)
                if result == True:
                    return [row,collum]
    if grid[1][1] == " ":
        return [1,1]


    #corner
    if grid[0][0] == " ":
        return [0,0]
    if grid[0][2] == " ":
        return [0,2]
    if grid[2][0] == " ":
        return [2,0]
    if grid[2][2] == " ":
        return [2,2]


    if grid[1][0] == " ":
        return [1,0]
    if grid[2][1] == " ":
        return [2,1]
    if grid[1][2] == " ":
        return [1,2]
    if grid[0][1] == " ":
        return [0,1]

'''
def random_o_move(grid):#random 0 place
    while True:
        r = random.randint(0,2)
        c = random.randint(0, 2)
        if grid[r][c] == " ":

            return [r,c]'''

l = random.randint(0,2)


printboard(grid)

while True:


    if l == 1:
        # AI TURN
        print("o turn")
        p = aipredict(grid)

        # if no winning/blocking move exists do random
        '''if p is None:
            p = random_o_move(grid)'''

        grid[p[0]][p[1]] = "o"

        l = 2

    else:# bc turn decision

        while True:#same
            print("x turn")
            row = int(input("pick a row to play:"))
            collum = int(input("pick a collum to play:"))

            if (row <= 2 and row >= 0) and (collum <= 2 and collum >= 0) and grid[row][collum] == " ":
                grid[row][collum] = "x"
                break

        # AI TURN
        print("o turn")

        p = aipredict(grid)

        # fallback random move
        '''if p is None:
            p = random_o_move(grid)'''

        grid[p[0]][p[1]] = "o"

    printboard(grid)

    # CHECK WINNER HERE
    if win(grid, "x") == True:
        print("player X wins!")
        break

    if win(grid, "o") == True:
        print("player O wins!")
        break



