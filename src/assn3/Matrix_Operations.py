import numpy as np
from fractions import Fraction


# alters array into reduced row echelon form
def rref(arr, show_steps=False):
	arr = np.array(arr, dtype=float)
	big = max(arr.shape)
	completed_rows = 0
	pivot_col = 0

	for i in range(big):
		# make sure pivot row  and col is not zero or else swap
		pivot = get_pivot(arr, pivot_col, completed_rows)
		if pivot != -1:

			# row swap to get a nice diagonal of one's
			if completed_rows != pivot:
				arr[[completed_rows, pivot]] = arr[[pivot, completed_rows]]
				if show_steps:
					print(f"Swap R{pivot+1} and R{completed_rows+1}")
					print(arr)

			arr = zero_col(arr, pivot_col, completed_rows, show_steps)
			completed_rows += 1

		# denotes a column of zeros
		else:
			pass

		pivot_col += 1

	return arr


def get_pivot(arr, col: int, completed_rows)->int:
	# return -1 if entire col is already zero
	# else return the row that will be the next pivot
	# will return the largest available value in the column to reduce numerical instability of
	# dividing numbers by small numbers

	try:
		max_value = 0
		max_row = 0
		for row in range(arr.shape[0]-completed_rows):
			val = arr[completed_rows][col]

			# find the next largest value in the pivot column to avoid numerical instability
			if abs(val) > abs(max_value):
				max_value = val
				max_row = completed_rows
			completed_rows += 1

		# the column is full of zeros
		if max_value == 0:
			return -1
		# returns next pivot row
		return max_row

	except IndexError:
		return -1


# makes all values in a column, except the pivot, zero
# used to make a matrix RREF
def zero_col(arr, pivot_col, pivot, show_steps=False):
	# dividing everything py the pivot
	pivot_val = arr[pivot][pivot_col]
	arr[pivot] = arr[pivot] / pivot_val
	if show_steps:
		print(f"R{pivot+1} / {pivot_val}")
		print(arr)

	for row in range(arr.shape[0]):
		if row == pivot:
			pass
		else:
			row_value = arr[row][pivot_col]

			if show_steps:
				# adding one to the row printout for better math notation
				print(f"R{row+1} - {row_value}*R{pivot+1}")
			arr[row] = arr[row] - row_value * arr[pivot]

			if show_steps:
				print(arr)

	return arr


# makes everything below the pivot zero
# Used with forward elimination to make an upper triangular matrix
def zeros_below(arr, pivot_col, pivot, show_steps=False):
	pivot_val = arr[pivot][pivot_col]
	arr[pivot] = arr[pivot] / pivot_val
	if show_steps:
		print(f"R{pivot+1} / {pivot_val}")
		print(arr)

	for row in range(pivot + 1, arr.shape[0]):
		row_value = arr[row][pivot_col]

		if show_steps:
			# adding one to the row printout for better math notation
			print(f"R{row+1} - {row_value}*R{pivot+1}")
		arr[row] = arr[row] - row_value * arr[pivot]

		if show_steps:
			print(arr)
	return arr


def to_fraction(arr):
	arr = arr.astype('object')
	for row in range(arr.shape[0]):
		for col in range(arr.shape[1]):
			arr[row][col] = Fraction(arr[row][col])
	return arr


def forward_elimination(arr, show_steps=False):
	arr = np.array(arr, dtype=float)
	big = max(arr.shape)
	completed_rows = 0
	pivot_col = 0

	for i in range(big):
		# make sure pivot row  and col is not zero or else swap
		pivot = get_pivot(arr, pivot_col, completed_rows)
		if pivot != -1:

			# row swap to get a nice diagonal of one's
			if completed_rows != pivot:
				arr[[completed_rows, pivot]] = arr[[pivot, completed_rows]]
				if show_steps:
					print(f"Swap R{pivot+1} and R{completed_rows+1}")
					print(arr)

			arr = zeros_below(arr, pivot_col, completed_rows, show_steps)
			completed_rows += 1

		# denotes a column of zeros
		else:
			pass

		pivot_col += 1

	return arr


# assumes that arr is already in a upper triangle with a main diagonal of ones
def back_substitute(arr, show_steps=False):
	solutions = {}
	for i in range(arr.shape[0]-1, -1, -1):
		sum_of_other_terms = 0.0
		for sol in solutions:
			sum_of_other_terms += arr[i][sol] * solutions[sol]

		x = arr[i][-1] - sum_of_other_terms

		if show_steps:
			print(f"X{i} is {x}")
		solutions[i] = x

	return solutions

# assumes that arr is already in a lower triangle with a main diagonal of ones
def forward_substitute(arr, show_steps=False):
	solutions = {}
	for i in range(arr.shape[0]):
		sum_of_other_terms = 0.0
		for sol in solutions:
			sum_of_other_terms += arr[i][sol] * solutions[sol]
		x = arr[i][-1] - sum_of_other_terms

		if show_steps:
			print(f"X{i} is {x}")
		solutions[i] = x

	return solutions


def gauss_jordan_elimination(arr, show_steps=False):
	arr = forward_elimination(arr, show_steps)
	solutions = back_substitute(arr, show_steps)
	return solutions


# assumes the arr is already in a upper triangle
def lu_decomposition(arr, show_steps=False):
	arr = forward_elimination(arr, show_steps)
	print(arr)

# arr must be square to have an inverse
def inverse(arr):
	inv = np.zeros(arr.shape, dtype=float)
	identity = np.identity(arr.shape[0])


	#L Z = C_v
	# forward solve for the z vector three times for the three vectors of the identity matrix (C)
	# U X = Z
	# back solve for x, where x is the identity vector
