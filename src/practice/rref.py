import numpy as np


def swap(array, row1, row2):
	array[row1], array[row2] = array[row2], array[row1].copy()


a = np.array([
	[2, 0, 1],
	[8, 4, 1],
	[1, 3, 0]
])

a = np.matrix(a)

# print(a[:, :2])  # first two columns

swap(a, 1, 2)

print(a)

print(min(a[:,0]))