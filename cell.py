from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = Point(self._x2, self._y2)
        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)
        else:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, "white")
        if self.has_left_wall:
            left_wall = Line(top_left, bot_left)
            self._win.draw_line(left_wall)
        else:
            left_wall = Line(top_left, bot_left)
            self._win.draw_line(left_wall, "white")
        if self.has_right_wall:
            right_wall = Line(top_right, bot_right)
            self._win.draw_line(right_wall)
        else:
            right_wall = Line(top_right, bot_right)
            self._win.draw_line(right_wall, "white")
        if self.has_bottom_wall:
            bot_wall = Line(bot_left, bot_right)
            self._win.draw_line(bot_wall)
        else:
            bot_wall = Line(bot_left, bot_right)
            self._win.draw_line(bot_wall, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "grey"
        half1 = abs(self._x2 - self._x1) // 2
        start = Point(self._x1 + half1, self._y1 + half1) 

        half2 = abs(to_cell._x2 - to_cell._x1) // 2
        end = Point(to_cell._x1 + half2, to_cell._y1 + half2)
        move_line = Line(start, end)
        self._win.draw_line(move_line, color)