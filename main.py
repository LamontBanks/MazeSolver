from graphics import *
from cell import * 

def main():
    window = Window(800, 600)

    # pointa = Point(100, 100)
    # pointb = Point(600, 600)
    # line = Line(pointa, pointb)
    # window.draw_line(line)

    wall_length = 100

    cell1 = Cell(window)
    cell1.draw(50, 50, 50 + wall_length, 50 + wall_length)

    cell2 = Cell(window)
    cell2.draw(300, 50, 300 + wall_length, 50 + wall_length)

    cell1.draw_move(cell2)

    window.wait_for_close()

main()