def add_new_tile(grid):
    x, y = random.randint(0, 3), random.randint(0, 3)
    while grid[x][y] != 0:
        x, y = random.randint(0, 3), random.randint(0, 3)
    grid[x][y] = 4 if random.random() > 0.9 else 2
