from tkinter import Tk, BOTH, Canvas
from window import Window
from maze import Maze

def main():
	win = Window(800, 600)
	maze = Maze(5, 5, 25, 25, 20, 20, win)
	maze.solve()
	win.wait_for_close()

main()
