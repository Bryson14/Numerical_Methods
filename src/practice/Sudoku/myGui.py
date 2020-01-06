import pygame
import time
from .sudoku_solver import AllBoards

pygame.font.init()

class board:
	all_boards = AllBoards()
	board = all_boards[0].board

	def __init__(self, rows, cols, width, height, win):
		self.rows = rows
		self.cols = cols
		self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
		self.width = width
		self.height = height
		self.model = None
		self.update_model()
		self.selected = None
		self.win = win


class Cube:
	ROWS = 9
	COLS = 9

	def __init__(self, value, row, col, width, height):
		self.value = value
		self.temp = 0
		self.row = row
		self.col = col
		self.width = width
		self.height = height
		self.selected = False

	def draw(self, win):
		fnt = pygame.font.SysFont("comicsans", 40)

