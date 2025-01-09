from graphics import *
from maze import *

def main():
    window = Window(800, 600)

    maze = Maze(50, 50, 8, 10, 50, 50, window)
    maze._create_cells()

    maze._break_entrance_and_exit()
    maze._break_walls_recursive(0, 0)

    window.wait_for_close()

main()