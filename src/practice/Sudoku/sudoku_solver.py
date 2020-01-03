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
		# self.solve()

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

		lst = [0, 0]
		if not self.find_next_empty(lst):
			return True

		for num in range(1, self.size + 1):
			if self.is_valid(num, lst[0], lst[1]):

				self.solution[lst[0]][lst[1]] = num

				# return if success
				if self.solve():
					return True

				# failure, reset
				self.solution[lst[0]][lst[1]] = 0

		return False

	def find_next_empty(self, lst):
		row, col = self.solution.shape
		for i in range(row):
			for j in range(col):
				if self.solution[i][j] == 0:
					lst[0] = i
					lst[1] = j
					return True

		return False

	# works for pre-checking a move. Makes sure a certain number doesn't already exist in a blocking space
	def is_valid(self, value, r_idx, c_idx):

		if value in self.solution[:, c_idx] or value in self.solution[r_idx]:
			return False

		# refers to which third, or part of the board the value is in. If the board is not
		# the traditional 3x3, then it may be of another size
		v_part = r_idx // self.chunk_size
		h_part = c_idx // self.chunk_size

		start_row = v_part * self.chunk_size
		end_row = start_row + self.chunk_size
		start_col = h_part * self.chunk_size
		end_col = start_col + self.chunk_size

		if value in self.solution[start_row:end_row, start_col:end_col]:
			return False

		else:
			return True


class AllBoards:
	def __init__(self):

		file_name = Path.joinpath(Path.cwd(), "sudoku_boards.txt")

		self.puzzles = []
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
							self.puzzles.append(Sudoku(puzzle_str, size))
							puzzle_str = ""
							lines = 0

		except ValueError as e:
			print("uh oh")
			print(e)


		for i in range(len(self.puzzles)):
			self.puzzles[i].solve()


a = AllBoards()
print(a.puzzles[1].solution)