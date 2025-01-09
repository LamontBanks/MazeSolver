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


if __name__ == "__main__":
    unittest.main()