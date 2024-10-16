def reverse(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(3, -1, -1):
            new_grid[i].append(grid[i][j])
    return new_grid
