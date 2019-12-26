from pathlib import Path
import numpy as np


class Sudoku:
	def __init__(self, board_str, board_size):
		self.board_str = board_str
		acceptable_sizes = [4, 9, 16, 25]
		if board_size in acceptable_sizes:
			self.size = board_size
		else:
			self.size = 9
		self.board = []
		self.create_board()
		self.solution = self.board.copy()
		self.solve()

	def create_board(self):
		for line in self.board_str.split("\n"):
			if line != "":
				self.board.append(line.split())

		for row in range(self.size):
			for col in range(self.size):
				if self.board[row][col] != "":
					self.board[row][col] = int(self.board[row][col])

		self.board = np.array(self.board)

	def solve(self):
		# backtracking algorithm
		pass

	def is_valid(self, r_idx, c_idx):
		pass


file_name = Path.joinpath(Path.cwd(), "sudoku_boards.txt")

puzzles = []
puzzle_str = ""
try:
	with open(file_name) as data:
		lines = 0
		for line in data.readlines():
			if line == "\n":
				pass
			elif len(line) < 5:
				size = int(line)
			else:
				# line of data
				puzzle_str += line
				lines += 1
				if lines >= size:
					puzzles.append(Sudoku(puzzle_str, size))
					puzzle_str = ""
					lines = 0

except ValueError as e:
	print("uh oh")
	print(e)

print(puzzles)
