from tkinter import Tk, BOTH, Canvas

"""Open a new window with a blank canvas that the program will then draw on."""
class Window:
    """
        width, height - size of the window in pixels
    """
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title = 'Maze Solver'

        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack()
        self._window_is_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    # Draw a line

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

    def draw_cell(self, cell, fill_color="black"):
        cell.draw(self._canvas, fill_color)

    # Boilerplate

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._window_is_running = True
        while self._window_is_running:
            self.redraw()

    def close(self):
        self._window_is_running = False
        
"""
x - the x-coordinate (horizontal) in pixels of the point
y - the y-coordinate (vertical) in pixels of the point
-
x = 0 is the left of the screen
y = 0 is the top of the screen
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

"""
Line is defined by 2 Point()
"""
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    """
        canvas - TKinter Canvas
        fill_color = string like "black" or "red"
    """
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )


