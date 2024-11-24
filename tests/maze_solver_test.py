import unittest

from context import maze 
from context import window







class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = window.Window(1024,768)
        num_cols = 12
        num_rows = 10
        m1 = maze.Maze(0, 0, num_rows, num_cols, 10, 10,win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_odd(self):
        win = window.Window(1024,768)
        num_cols = 9
        num_rows = 7
        m1 = maze.Maze(0, 0, num_rows, num_cols, 10, 10,win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_bigger(self):
        win = window.Window(1024,768)
        num_cols = 20
        num_rows = 18
        m1 = maze.Maze(0, 0, num_rows, num_cols, 10, 10,win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_break_walls(self):
        win = window.Window(1024,768)
        num_cols = 5
        num_rows = 5
        m1 = maze.Maze(0, 0, num_rows, num_cols, 10, 10,win)
        m1.generate_maze()
        m1._reset_cells_visited()
        self.assertEqual(
            False,
            m1._cells[0][0].visited
        )
        self.assertEqual(
            False,
            m1._cells[3][2].visited
        )

if __name__ == "__main__":
    unittest.main()