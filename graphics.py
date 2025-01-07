from tkinter import Tk, BOTH, Canvas

"""Open a new window with a blank canvas that the program will then draw on."""
class Window:
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

    # Draw a line

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell, fill_color="black"):
        cell.draw(self.__canvas, fill_color)

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
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

"""
point_1 - Point()
point_2 - Point()
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

"""Represent a cell of the maze
    window - Window()
    x - left to right, y top to bottom
    x1, y1, is the upper-left corner
    x2, y2 is the lower-right corner
"""
class Cell:
    def __init__(self, window):
        # All walls exist by default
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self.__window = window

    # Draws the required walls of the cell
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        walls = []

        if self.has_left_wall:
            walls.append(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)))
        if self.has_right_wall:
            walls.append(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)))
        if self.has_top_wall:
            walls.append(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)))
        if self.has_bottom_wall:
            walls.append(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)))

        for wall in walls:
            self.__window.draw_line(wall)