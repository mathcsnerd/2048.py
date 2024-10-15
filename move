def move_left(grid):
    compressed = compress(grid)
    merged = merge(compressed)
    return compress(merged)

def move_right(grid):
    reversed_grid = reverse(grid)
    moved_grid = move_left(reversed_grid)
    return reverse(moved_grid)

def move_up(grid):
    transposed_grid = transpose(grid)
    moved_grid = move_left(transposed_grid)
    return transpose(moved_grid)

def move_down(grid):
    transposed_grid = transpose(grid)
    moved_grid = move_right(transposed_grid)
    return transpose(moved_grid)
