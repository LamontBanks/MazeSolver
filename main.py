from graphics import *
from maze import *

def main():
    window = Window(800, 600)

    maze = Maze(50, 50, 14, 10, 50, 50, window)
    maze.solve()

    window.wait_for_close()

main()