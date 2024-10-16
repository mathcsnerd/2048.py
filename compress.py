def compress(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                pos += 1
    return new_grid
