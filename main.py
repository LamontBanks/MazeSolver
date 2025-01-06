from graphics import *

def main():
    window = Window(800, 600)

    point1a = Point(100, 100)
    point1b = Point(600, 600)

    point2a = Point(323, 424)
    point2b = Point(9, 9)

    point3a = Point(3, 3)
    point3b = Point(500, 432)

    line1 = Line(point1a, point1b)
    line2 = Line(point2a, point2b)
    line3 = Line(point3a, point3b)

    window.draw_line(line1)
    window.draw_line(line2)
    window.draw_line(line3)

    window.wait_for_close()

main()