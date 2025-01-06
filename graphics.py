from tkinter import Tk, BOTH, Canvas

"""Open a new window with a blank canvas that the program will then draw on."""
class Window():
    """
        width, height - size of the window in pixels
    """
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = 'Maze Solver'

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__window_is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # Draw

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    # Boilerplate

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_is_running = True
        while self.__window_is_running:
            self.redraw()

    def close(self):
        self.__window_is_running = False
        
"""
x - the x-coordinate (horizontal) in pixels of the point
y - the y-coordinate (vertical) in pixels of the point
-
x = 0 is the left of the screen
y = 0 is the top of the screen
"""
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

"""
point_1 - Point()
point_2 - Point()
"""
class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    """
        canvas - TKinter Canvas
        fill_color = string like "black" or "red"
    """
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2
        )