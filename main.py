import random
import os
import sys

def main():
    grid = start_game()
    while True:
        print_grid(grid)
        if check_game_over(grid):
            print("Game Over!")
            break
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['a', 'd', 'w', 's']:
            if move == 'a':
                new_grid = move_left(grid)
            elif move == 'd':
                new_grid = move_right(grid)
            elif move == 'w':
                new_grid = move_up(grid)
            elif move == 's':
                new_grid = move_down(grid)

            if new_grid != grid:
                grid = new_grid
                add_new_tile(grid)

if __name__ == "__main__":
    main()
