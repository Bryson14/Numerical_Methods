import numpy as np
from assn3.Matrix_Operations import rref, gauss_jordan_elimination

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
three = np.array([
	[8, 4, -1, 11],
	[-2, 5, 1, 4],
	[2, -1, 6, 7]
])
four = np.array([
	[2, -6, -1, -38],
	[-3, -1, 7, -34],
	[-8, 1, -2, -20]
])

arrays = [one, two, three, four]
i = 1
# for arr in arrays:
# 	print(i)
# 	print(rref(arr))
# 	i += 1

print("given the following array:")
print(arrays[1])
print("Here is the produced solution")
print(gauss_jordan_elimination(arrays[1], True))
