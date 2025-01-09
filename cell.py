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
        
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self._window = window

    # Draws the required walls of the cell
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        walls = []

        if self.has_left_wall:
            walls.append(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            walls.append(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            walls.append(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            walls.append(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))

        for wall in walls:
            self._window.draw_line(wall)

    """
    Draws a line from the center of one cell to another
    is_undo_line indicates toggles the line color between red and gray to indicate if a line currently part of the final path
    """
    def draw_move(self, dest_cell, is_undo_line=False):
        fill_color = "red" if not is_undo_line else "gray"

        # Find the center point of both cells
        source_center_x = self._x1 + (abs((self._x2 - self._x1)) // 2)
        source_center_y = self._y1 + (abs((self._y2 - self._y1)) // 2)
        dest_center_x = dest_cell._x1 + (abs((dest_cell._x2 - dest_cell._x1)) // 2)
        dest_center_y = dest_cell._y1 + (abs((dest_cell._y2 - dest_cell._y1)) // 2)

        line = Line(Point(source_center_x, source_center_y), Point(dest_center_x, dest_center_y))

        self._window.draw_line(line, fill_color)