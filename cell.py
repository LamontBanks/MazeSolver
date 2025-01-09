from graphics import Line, Point

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
        
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None

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

    """
    Draws a line from the center of one cell to another
    is_undo_line indicates toggles the line color between red and gray to indicate if a line currently part of the final path
    """
    def draw_move(self, dest_cell, is_undo_line=False):
        fill_color = "red" if not is_undo_line else "gray"

        # Find the center point of both cells
        source_center_x = self.__x1 + (abs((self.__x2 - self.__x1)) // 2)
        source_center_y = self.__y1 + (abs((self.__y2 - self.__y1)) // 2)
        dest_center_x = dest_cell.__x1 + (abs((dest_cell.__x2 - dest_cell.__x1)) // 2)
        dest_center_y = dest_cell.__y1 + (abs((dest_cell.__y2 - dest_cell.__y1)) // 2)

        line = Line(Point(source_center_x, source_center_y), Point(dest_center_x, dest_center_y))

        self.__window.draw_line(line, fill_color)