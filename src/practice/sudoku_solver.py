from pathlib import Path
import numpy as np
import math


class Sudoku:
	def __init__(self, board_str, board_size):
		self.board_str = board_str
		acceptable_sizes = [4, 9, 16, 25]
		if board_size in acceptable_sizes:
			self.size = board_size
		else:
			self.size = 9
		self.chunk_size = int(math.sqrt(self.size))
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

	# works for prechecking a move. Makes sure a certain number doesn't already exist in a blocking space
	def is_valid(self, value, r_idx, c_idx):

		if value in self.board[:, c_idx] or value in self.board[r_idx]:
			return False


		# refers to which third, or part of the board the value is in. If the board is not
		# the traditional 3x3, then it may be of another size
		v_part = r_idx//self.chunk_size
		h_part = c_idx//self.chunk_size

		start_row = v_part*self.chunk_size
		end_row = start_row + self.chunk_size
		start_col = h_part * self.chunk_size
		end_col =start_col + self.chunk_size

		if value in self.board[start_row:end_row, start_col:end_col]:
			return False

		else:
			return True


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
