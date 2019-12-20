import numpy as np


def rref(arr):
	small = min(arr.shape)
	completed_rows = 0
	pivot_col = 0

	while completed_rows < small:
		# make sure pivot row  and col is not zero or else swap
		pivot = get_pivot(arr, pivot_col, completed_rows)
		if pivot != -1:

			arr = zero_col(arr, pivot_col, pivot)
		pivot_col += 1

	return arr


def get_pivot(arr, col:int, completed_rows)->int:
	# return -1 if entire col is already zero
	# else return the row that will be the next pivot

	try:
		for row in arr.shape[0]:
			val = arr[completed_rows][col]
			if val != 0:
				return completed_rows

	except IndexError:
		return -1
	return completed_rows


def zero_col(arr, pivot_col, pivot):
	return arr


a = np.array([
	[1, 2, 3],
	[2, 4, 1]
])

print(a[2][2])