from tkinter import Tk
import time
import random
from cell import Cell
from window import Window

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                position_x1 = self._x1 + (i * self._cell_size_x)
                position_y1 = self._y1 + (j * self._cell_size_y)
                position_x2 = position_x1 + self._cell_size_x
                position_y2 = position_y1 + self._cell_size_y
                cell = Cell(position_x1, position_y1, position_x2, position_y2, self._win)
                col.append(cell)
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

            

    def _draw_cell(self, i, j):
        if self._win is not None:
            cell = self._cells[i][j]
            cell.draw_cell()
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        start_cell.has_top_wall = False
        self._draw_cell(0, 0)

        bottom_cell = self._cells[-1][-1]
        bottom_cell.has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            chosen_cell = random.randrange(0, len(to_visit))
            next_i, next_j = to_visit[chosen_cell]

            if next_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            if next_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            if next_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            if next_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)
            self._break_walls_r(next_i, next_j)

        
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        if j > 0 and not self._cells[i][j-1].visited and self._cells[i][j].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        if j < self._num_rows-1 and not self._cells[i][j+1].visited and self._cells[i][j].has_bottom_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

        if i > 0 and not self._cells[i-1][j].visited and self._cells[i][j].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

        if i < self._num_cols-1 and not self._cells[i+1][j].visited and self._cells[i][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)

        return False

                        

                        



