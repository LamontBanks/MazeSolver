from cell import *
import time
import random

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
        self._break_entrance_and_exit()
        self._break_walls_recursive(0, 0)

    """Creates the entrance and exit of the maze
    The entrance to the maze will always be at the top of the top-left cell, the exit always at the bottom of the bottom-right cell.
    """
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]

        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    """Random break walls between cells to create the actual maze.
    Uses depth-first traversal
    """
    def _break_walls_recursive(self, col, row):
        # Visit the current cell
        curr_cell = self._cells[col][row]
        curr_cell.visited = True

        while True:
            # Get all adjacent cells, then the unvisited cells
            adjacent_cells = self._adjacent_cells(col, row)
            unvisited_cells = list(filter(lambda cell_tuple: cell_tuple[0].visited == False, adjacent_cells))

            # If there are no directions to go in, draw the currect cell and return
            if len(unvisited_cells) == 0:
                self._draw_cell(col, row)
                return

            # Otherwise, choose a random adjacent cell and remove the walls between it and this cell
            next_cell_tuple = unvisited_cells[random.randint(0, len(unvisited_cells) - 1)]
            next_cell = next_cell_tuple[0]
            next_cell_col, next_cell_row = next_cell_tuple[1]

            # Determine which walls to remove:
            # Top
            # [next]
            #  ----
            #  ----
            # [curr]
            if next_cell_row < row:
                next_cell.has_bottom_wall = False
                curr_cell.has_top_wall = False
            # Bottom
            # [curr]
            #  ----
            #  ----
            # [next]
            elif next_cell_row > row:
                curr_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            # Left
            # [next] || [curr]
            elif next_cell_col < col:
                next_cell.has_right_wall = False
                curr_cell.has_left_wall = False
            # Right
            # [curr] || [next]
            elif next_cell_col > col:
                curr_cell.has_right_wall = False
                next_cell.has_left_wall = False

            # Move to the next cell and repeat
            self._break_walls_recursive(next_cell_col, next_cell_row)

    """Finds the path from the start (upper-left corner: 0,0) to the end (lower-left corner: max col, row)"""
    def solve(self, show_attempted_paths=False):
        self._reset_cells_visited()
        # return self._solve_breadth_first_search(0, 0)
        return self._solve_depth_first_search(0, 0, show_attempted_paths)
    
    def _solve_depth_first_search(self, col, row, show_attempted_paths):
        self._animate()
        
        # Mark the current cell as visited
        curr_cell = self._cells[col][row]
        curr_cell.visited = True

        # Return if we've reached the end
        if col == self._num_cols - 1 and row == self._num_rows - 1:
                return True
        
        # Get adjacent, traversible cells (based on walls), then filter for unvisted
        neighbors = self._adjacent_traversible_cells(col, row)
        neighbors = list(filter(lambda cell_tuple: cell_tuple[0].visited == False, neighbors))

        for neighbor in neighbors:
            neighbor_cell = neighbor[0]
            neighbor_cell_col, neighbor_cell_row = neighbor[1]
            curr_cell.draw_move(neighbor_cell)

            check_other_paths = self._solve_depth_first_search(neighbor_cell_col, neighbor_cell_row, show_attempted_paths)
            if check_other_paths:
                return True
            else:
                curr_cell.draw_move(neighbor_cell, is_undo_line=True, is_visible_undo_line=show_attempted_paths)
        
        return False

    """TODO: Finds the path, but doesn't "undo" alternate paths"""
    def _solve_breadth_first_search(self, col, row):
        to_visit = []
        visited = []

        curr_cell = self._cells[col][row]
        to_visit.append((curr_cell, (col, row)))

        while (col != self._num_cols - 1) and (row != self._num_rows - 1):
            self._animate()

            # Go to the next cell
            curr_cell_tuple = to_visit.pop(0)
            curr_cell = curr_cell_tuple[0]
            curr_cell_col, curr_cell_row = curr_cell_tuple[1]
            
            # Mark it as visited
            curr_cell.visited = True
            visited.append(curr_cell_tuple)

            # If the maze exit has been reached, stop
            if curr_cell_col == self._num_cols - 1 and curr_cell_row == self._num_rows - 1:
                return visited

            # Get adjacent, traversible cells (based on walls)
            neighbors = self._adjacent_traversible_cells(curr_cell_col, curr_cell_row)

            for neighbor in neighbors:
                neighbor_cell = neighbor[0]
                if (neighbor not in visited) and (neighbor not in to_visit):
                    to_visit.append(neighbor)
                    curr_cell.draw_move(neighbor_cell)

        return visited
            
    """Return a list of tuples containing the adjacent cells (if any) and their col, row coordinates.
        Format: (Cell, (col, row)) 
    Don't rely on the cells being listed in a particular order (i.e., top, bottom, ..., etc.)"""
    def _adjacent_cells(self, col, row):
        cells = []

        # left
        if 0 <= col - 1:
            cells.append((self._cells[col - 1][row], (col - 1, row)))
        # right
        if col + 1 <= self._num_cols - 1:
            cells.append((self._cells[col + 1][row], (col + 1, row)))
        # top
        if row - 1 >= 0:
            cells.append((self._cells[col][row - 1], (col, row - 1)))
        # bottom
        if row + 1 <= self._num_rows - 1:
            cells.append((self._cells[col][row + 1], (col, row + 1)))

        return cells
    
    """Return a list of tuples containing the adjacent cells *without adjacent walls*, and their col,row coordinates.
        Format: (Cell, (col, row)) 
    Don't rely on the cells being listed in a particular order (i.e., top, bottom, ..., etc.)"""
    def _adjacent_traversible_cells(self, col, row):
        cells = []

        # left
        if 0 <= col - 1:
            left_cell = self._cells[col - 1][row]
            if not left_cell.has_right_wall:
                cells.append((left_cell, (col - 1, row)))
        # right
        if col + 1 <= self._num_cols - 1:
            right_cell = self._cells[col + 1][row]
            if not right_cell.has_left_wall:
                cells.append((right_cell, (col + 1, row)))
        # top
        if row - 1 >= 0:
            top_cell = self._cells[col][row - 1]
            if not top_cell.has_bottom_wall:
                cells.append((top_cell, (col, row - 1)))
        # bottom
        if row + 1 <= self._num_rows - 1:
            bottom_cell = self._cells[col][row + 1]
            if not bottom_cell.has_top_wall:
                cells.append((bottom_cell, (col, row + 1)))

        return cells
    
    """"Resets cell visisted flags to False"""
    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False


    """Creates and draws the initial cells"""
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

    """Draws the cell located at col, row on the maze"""
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
        time.sleep(0.025)