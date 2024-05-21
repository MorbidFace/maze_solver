import time
import random
from cell import Cell

class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

        if seed != None:
            random.seed(seed)

        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(0, self._num_cols):
            row = []
            for j in range(0, self._num_rows):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)

        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = (i * self._cell_size_x) + self._x1
        y1 = (j * self._cell_size_y) + self._y1
        x2 = (x1 + self._cell_size_x) 
        y2 = (y1 + self._cell_size_y)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            if i != 0:
                if not self._cells[i-1][j].visited:
                    cells_to_visit.append((i-1, j, 'left'))
            if i != self._num_cols-1:
                if not self._cells[i+1][j].visited:
                    cells_to_visit.append((i+1, j, 'right'))
            if j != 0:
                if not self._cells[i][j-1].visited:
                    cells_to_visit.append((i, j-1, 'up'))
            if j != self._num_rows-1:
                if not self._cells[i][j+1].visited:
                    cells_to_visit.append((i, j+1, 'down'))
            if len(cells_to_visit) == 0:
                self._draw_cell(i, j)
                return
            dir = random.randint(0, len(cells_to_visit)-1)
            chosen_col =cells_to_visit[dir][0]
            chosen_row =cells_to_visit[dir][1]
            if cells_to_visit[dir][2] == 'left':
                self._cells[i][j].has_left_wall = False
                self._cells[chosen_col][chosen_row].has_right_wall = False
            elif cells_to_visit[dir][2] == 'right':
                self._cells[i][j].has_right_wall = False
                self._cells[chosen_col][chosen_row].has_left_wall = False
            elif cells_to_visit[dir][2] == 'up':
                self._cells[i][j].has_top_wall = False
                self._cells[chosen_col][chosen_row].has_bottom_wall = False
            elif cells_to_visit[dir][2] == 'down':
                self._cells[i][j].has_bottom_wall = False
                self._cells[chosen_col][chosen_row].has_top_wall = False
            self._break_walls_r(chosen_col, chosen_row)

    def _reset_cells_visited(self):
            for i in range(self._num_cols):
                for j in range(self._num_rows):
                    self._cells[i][j].visited = False
                
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        # right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        # up
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        # down
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False