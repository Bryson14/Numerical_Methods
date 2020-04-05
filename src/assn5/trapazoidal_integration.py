import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = 3 * np.power(x, 2) + 5*x - 7
    return y

# Enter Bounds Here and Number of SubIntervals
a = 0
b = 5
n = 100

def trap_integration():
    # creates the step size
    step = (b - a) / n
    # adds the sum of the evaluation of the function at each step from a to b
    iter_sum = function(a) + function(b) + sum(list(map(lambda x: 2 * function(x), np.arange(a + step, b, step))))
    # alters the sum by the range of the bounds and 2n
    return (b - a) * iter_sum / (2 * n)

print(trap_integration())