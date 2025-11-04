grid = []

for i in range(30):
    row = []
    for i in range(60):
        row.append(False)

    grid.append(row)
grid[11][31] = True


def printboard(grid):
    for line in grid:
        for thing in line:
            if thing == False:
                print("-", end="")
            else:
                print("O", end="")
        print()


printboard(grid)

