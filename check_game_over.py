def check_game_over(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
            if grid[i][j] == 0:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
    return True
