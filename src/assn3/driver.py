import numpy as np
from assn3.Matrix_Operations import rref, gauss_jordan_elimination, lu_decomposition, inverse, sol_lu_decomposition

one = np.array([
	[10, 2, -1, 27],
	[-3, -6, 2, -61.5],
	[1, 1, 5, -21.5]
])
two = np.array([
	[1, 2, -1, 2],
	[5, 2, 2, 9],
	[-3, 5, -1, 1]
])
three_total = np.array([
	[8, 4, -1, 11],
	[-2, 5, 1, 4],
	[2, -1, 6, 7]
])
three = np.array([
	[8, 4, -1],
	[-2, 5, 1],
	[2, -1, 6]
])
three_rh = np.array([
	[11],
	[4],
	[7]
])
four_total = np.array([
	[2, -6, -1, -38],
	[-3, -1, 7, -34],
	[-8, 1, -2, -20]
])

four = np.array([
	[2, -6, -1],
	[-3, -1, 7],
	[-8, 1, -2]
])
four_rh = np.array([
	[-38],
	[-34],
	[-20]
])
five = np.array([
	[3,   1, 8, -2],
	[-4, -2, 1,  0],
	[8,  -9, 2,  1],
	[5,   9, 5,  0]
])

arrays = [one, two, three, four, four_rh, five]

print(sol_lu_decomposition(three, three_rh))
# print(inverse(three))