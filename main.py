from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 8, 8, 60, 60, win)
    maze.solve()
    win.wait_for_close()


main()