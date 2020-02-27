import numpy as np
import sys


# assumes that arr is already in a upper triangle
def back_substitute(arr, show_steps=False):
    solutions = {}
    for i in range(arr.shape[0] - 1, -1, -1):
        sum_of_other_terms = 0.0
        for sol in solutions:
            sum_of_other_terms += arr[i][sol] * solutions[sol]

        x = (arr[i][-1] - sum_of_other_terms) / arr[i][i]

        if show_steps:
            print(f"X{i} is {x}")
        solutions[i] = x

    return np.array([solutions[i] for i in range(arr.shape[0])])


# assumes that arr is already in a lower triangle
def forward_substitute(arr, show_steps=False):
    solutions = {}
    for i in range(arr.shape[0]):
        sum_of_other_terms = 0.0
        for sol in solutions:
            sum_of_other_terms += arr[i][sol] * solutions[sol]
        x = (arr[i][-1] - sum_of_other_terms) / arr[i][i]

        if show_steps:
            print(f"X{i} is {x}")
        solutions[i] = x

    return np.array([solutions[i] for i in range(arr.shape[0])])


# must be a square matrix
# best resource for visualizing LU decomposition
# https://epxx.co/artigos/ludecomp.html
def lu_decomposition(arr, show_steps=False):
    arr = np.array(arr, dtype=float)

    try:
        assert arr.shape[0] == arr.shape[1]
    except AssertionError:
        print(f"Matrix must be a square matrix in order to be decomposed\n Matrix's shape was {arr.shape}")
        sys.exit(-1)

    side = arr.shape[0]
    L = np.identity(side)
    U = np.identity(side)

    # walks from left to right through arr
    for col in range(side):

        # fills in U
        for row in range(col + 1):
            s = sum(U[k][col] * L[row][k] for k in range(row))
            U[row][col] = arr[row][col] - s

            if show_steps:
                print(f"L {L} \nU {U}\n")

        # fills in L
        for row in range(col + 1, side):
            s = sum(U[k][col] * L[row][k] for k in range(row))

            # avoid dividing by zero since this algorithm is not pivoting
            if U[col][col] != 0.0:
                L[row][col] = (arr[row][col] - s) / U[col][col]
            else:
                L[row][col] = (arr[row][col] - s)

            if show_steps:
                print(f"L {L} \nU {U}\n")

    return L, U


# does the exact same thing as the inverse except that the C matrix is not the identity matrix
def sol_lu_decomposition(arr, right_hand, show_steps=False):
    side = arr.shape[0]
    inv = np.zeros(arr.shape, dtype=float)
    identity = np.identity(arr.shape[0])
    L, U = lu_decomposition(arr, show_steps)

    # must makes the vector matrices 2-D to be able to stack with L and U matrices
    # adds the identity vector to L. makes L and augmented matrix by adding the solution vector
    z = forward_substitute(np.hstack((L, np.atleast_2d(right_hand))))
    x = back_substitute(np.hstack((U, np.atleast_2d(z).T)), show_steps)

    return x


left = np.array([
    [-2.03, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, -2.03, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, -2.03, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, -2.03, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, -2.03, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, -2.03, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, -2.03, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, -2.03, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, -2.03],

])

right = np.array([
    [-19.7],
    [0.3],
    [0.3],
    [0.3],
    [0.3],
    [0.3],
    [0.3],
    [0.3],
    [-99.7]
])

print(sol_lu_decomposition(left, right))