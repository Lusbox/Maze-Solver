from tkinter import Tk
from window import *

class Cell:
	def __init__(self, x1, y1, x2, y2, win=None):
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2
		self._win = win
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self.visited = False


	def draw_cell(self):
		if self._win is not None:
			if self.has_left_wall == True:
				self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
			else:
				self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white")
			if self.has_right_wall == True:
				self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
			else:
				self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white")
			if self.has_top_wall == True:
				self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
			else:
				self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white")
			if self.has_bottom_wall == True:
				self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
			else:
				self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white")


	def draw_move(self, to_cell, undo=False):
		start_point = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
		end_point = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
		color = "gray" if undo else "red"
								
		self._win.draw_line(Line(start_point, end_point), color)

		
