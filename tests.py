import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 56
        num_rows = 19
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        cell1 = m1._cells[0][0]
        cell2 = m1._cells[-1][-1]
        self.assertFalse(cell1.has_top_wall)
        self.assertFalse(cell2.has_bottom_wall)

    def test_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        cell1 = m1._cells[1][1]
        cell1.visited = True
        cell2 = m1._cells[-2][-2]
        cell2.visited = True
        m1._reset_cells_visited()
        self.assertFalse(cell1.visited)
        self.assertFalse(cell2.visited)

if __name__ == "__main__":
    unittest.main()