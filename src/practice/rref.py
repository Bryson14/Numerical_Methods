import numpy as np


def rref(arr):
	arr = np.array(arr, "float")
	small = min(arr.shape)
	completed_rows = 0
	pivot_col = 0

	while completed_rows < small:
		# make sure pivot row  and col is not zero or else swap
		pivot = get_pivot(arr, pivot_col, completed_rows)
		if pivot != -1:
			arr = zero_col(arr, pivot_col, pivot)
			completed_rows += 1

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
	pivot_value = arr[pivot][pivot_col]

	for row in range(arr.shape[0]):
		if row == pivot:
			pass
		else:
			row_value = arr[row][pivot_col]
			arr[row] = pivot_value * arr[row] - row_value * arr[pivot]

	return arr


a = np.array([
	[1, 2, 3],
	[0, 4, 1],
	[8, 5, 4]
])

f = np.array([
	[2, 1, 4],
	[4, 5, 1]
])

# assert zero_col(f, 0, 0) == np.array([1, 1], [0, 1])
print(rref(f))


