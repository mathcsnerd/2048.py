def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([grid[j][i] for j in range(4)])
    return new_grid
