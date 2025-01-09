from cell import *
import time

"""
Represents a grid of cells
"""
class Maze:
    def __init__(self, origin_x, origin_y, num_cols, num_rows, cell_size_x, cell_size_y, window=None):
        if num_cols == 0 or num_rows == 0:
            raise Exception(f"Maze cannot have 0 rows or columns: {num_cols} columns | {num_rows} rows")

        self._origin_x = origin_x
        self._origin_y = origin_y
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        # Create the cells
        # *** Cols are first, Rows second ***
        for col in range(self._num_cols):
            self._cells.append([])
            for row in range(self._num_rows):
                self._cells[col].append(Cell(self._window))

        # Draw the cells
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    """Draws the cell located at row, col on the maze"""
    def _draw_cell(self, col, row):
        if self._window is None:
            return

        # Calculate the upper-left corner
        draw_x = self._origin_x + (col * self._cell_size_x)
        draw_y = self._origin_y + (row * self._cell_size_y)

        # Get the cell, then pass in the calculated draw coordinates
        # *** Cols across, rows down ***
        cell = self._cells[col][row]
        cell.draw(draw_x, draw_y, draw_x + self._cell_size_x, draw_y + self._cell_size_y)

        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)