from cell import *
import time

"""
Represents a grid of cells
"""
class Maze:
    def __init__(self, origin_x, origin_y, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self.__origin_x = origin_x
        self.__origin_y = origin_y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []

    def _create_cells(self):
        # Create the cells
        # *** Cols are first, Rows second ***
        for col in range(self.__num_cols):
            self.__cells.append([])
            for row in range(self.__num_rows):
                self.__cells[col].append(Cell(self.__window))
                self._draw_cell(col, row)

    """Draws the cell located at row, col on the maze"""
    def _draw_cell(self, col, row):
        # Calculate the upper-left corner
        draw_x = self.__origin_x + (col * self.__cell_size_x)
        draw_y = self.__origin_y + (row * self.__cell_size_y)

        # Get the cell, then pass in the calculated draw coordinates
        # *** Cols across, rows down ***
        cell = self.__cells[col][row]
        cell.draw(draw_x, draw_y, draw_x + self.__cell_size_x, draw_y + self.__cell_size_y)

        self._animate()

    def _animate(self):
        self.__window.redraw()
        time.sleep(0.05)