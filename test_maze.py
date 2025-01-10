import unittest

from maze import Maze
from cell import Cell

# Note: python3 test_maze.py TestMaze.test_get_adajcent_cells
class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_zero_cols(self):
        num_cols = 0
        num_rows = 10

        with self.assertRaises(Exception):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        

    def test_maze_zero_rows(self):
        num_cols = 10
        num_rows = 0

        with self.assertRaises(Exception):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_maze_has_entrance_and_exit(self):
        # "Regular" sized maze
        num_cols = 10
        num_rows = 5
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)

        m1._break_entrance_and_exit()

        entrance_cell = m1._cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall)
        exit_cell = m1._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(exit_cell.has_bottom_wall)

        # Single cell maze
        num_cols = 1
        num_rows = 1
        m2 = Maze(0, 0, num_cols, num_rows, 10, 10)

        m2._break_entrance_and_exit()

        entrance_cell = m2._cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall)
        exit_cell = m2._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(exit_cell.has_bottom_wall)

    def test_get_adjacent_cells(self):
        # Center cell in 3x3 grid:
        #    0    1    2
        # 0 [ ]  [ ]  [ ]
        # 1 [ ]  [X]  [ ]
        # 2 [ ]  [ ]  [ ]
        col = 1
        row = 1
        num_cols = 3
        num_rows = 3
        maze = Maze(0, 0, num_cols, num_rows, 10, 10)

        adjacent_cells = maze._adjacent_cells(col, row)

        # 4 adjacent cells
        self.assertEqual(len(adjacent_cells), 4)

        # First element is a Cell
        for cell_tuple in adjacent_cells:
            self.assertIsInstance(cell_tuple[0], Cell)

        # Check for the correct adjacent cells
        col_row_coords = []
        for cell_tuple in adjacent_cells:
            col_row_coords.append(cell_tuple[1])
        # top
        self.assertIn((1, 0), col_row_coords)
        # bottom
        self.assertIn((1, 2), col_row_coords)
        # left
        self.assertIn((0, 1), col_row_coords)
        # right
        self.assertIn((2, 1), col_row_coords)

    def test_get_adjacent_cells_2(self):
        # Left cell in 3x3 grid:
        #    0    1    2
        # 0 [ ]  [ ]  [ ]
        # 1 [X]  [ ]  [ ]
        # 2 [ ]  [ ]  [ ]
        col = 0
        row = 1
        num_cols = 3
        num_rows = 3
        maze = Maze(0, 0, num_cols, num_rows, 10, 10)

        adjacent_cells = maze._adjacent_cells(col, row)

        # Adjacent cells count
        self.assertEqual(len(adjacent_cells), 3)

        # First element is a Cell
        for cell_tuple in adjacent_cells:
            self.assertIsInstance(cell_tuple[0], Cell)

        # Check for the correct adjacent cells
        col_row_coords = []
        for cell_tuple in adjacent_cells:
            col_row_coords.append(cell_tuple[1])
        # top
        self.assertIn((0, 0), col_row_coords)
        # bottom
        self.assertIn((0, 2), col_row_coords)
        # no left
        # right
        self.assertIn((1, 1), col_row_coords)

    def test_get_adjacent_cells_none(self):
        # Single cell
        #    0
        # 0 [X]
        col = 0
        row = 0
        num_cols = 1
        num_rows = 1
        maze = Maze(0, 0, num_cols, num_rows, 10, 10)

        adjacent_cells = maze._adjacent_cells(col, row)

        # Adjacent cells count
        self.assertEqual(len(adjacent_cells), 0)

    def test_reset_visited_flags(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_cols, num_rows, 10, 10)

        maze._break_walls_recursive(0, 0)

        # Checked there are visited nodes
        contain_visited_flag = False
        for col in range(num_cols):
            for row in range(num_rows):
                if maze._cells[col][row].visited:
                    contain_visited_flag = True
                    break
        self.assertTrue(contain_visited_flag)

        # Reset flags, check for none
        maze._reset_cells_visited()
        contain_visited_flag = False
        for col in range(num_cols):
            for row in range(num_rows):
                if maze._cells[col][row].visited:
                    contain_visited_flag = True
                    break
        self.assertFalse(contain_visited_flag)





if __name__ == "__main__":
    unittest.main()
    # Specific test
    # unittest.main(defaultTest='TestMaze.test_get_adjacent_cells_none')