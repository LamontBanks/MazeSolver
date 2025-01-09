import unittest

from maze import Maze

class Tests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()