import numpy as np
from fractions import Fraction
from decimal import Decimal


def rref(arr):
	arr = np.array(arr, np.float)
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

			arr = zero_col(arr, pivot_col, completed_rows)
			completed_rows += 1

		# denotes a column of zeros
		else:
			pass

		pivot_col += 1

	return arr


def get_pivot(arr, col:int, completed_rows)->int:
	# return -1 if entire col is already zero
	# else return the row that will be the next pivot

	try:
		for row in range(arr.shape[0]):
			val = arr[completed_rows][col]
			if val != 0:
				return completed_rows
			completed_rows += 1

	except IndexError:
		return -1
	return -1


def zero_col(arr, pivot_col, pivot):
	# dividing everything py the pivot
	arr[pivot] = arr[pivot] / arr[pivot][pivot_col]

	for row in range(arr.shape[0]):
		if row == pivot:
			pass
		else:
			row_value = arr[row][pivot_col]
			arr[row] = arr[row] - row_value * arr[pivot]

	return arr


def to_fraction(arr):
	arr = arr.astype('object')
	for row in range(arr.shape[0]):
		for col in range(arr.shape[1]):
			arr[row][col] = Fraction(arr[row][col])
	return arr


a = [np.random.randint(0, 25, 6) for i in range(5)]
a = np.array(a)
print(a)
print(rref(a))

b = np.array([
	[-1,1,8],
	[-1,0,15],
])
print(rref(b))
