from graphics import *

def main():
    window = Window(800, 600)

    # pointa = Point(100, 100)
    # pointb = Point(600, 600)
    # line = Line(pointa, pointb)
    # window.draw_line(line)

    cell = Cell(window)

    cell.has_left_wall = False
    cell.has_bottom_wall = False
    cell.draw(200, 300, 500, 400)

    window.wait_for_close()

main()