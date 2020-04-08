import numpy as np
import time

def double_trap_integration(a, b, c, d, n, function):

    step = (d - c) / n
    y_steps = np.arange(c + step, d, step)
    iter_sum = trap_int(a, b, c, n, function) + trap_int(a, b, d, n, function) + \
               sum(list(map(lambda y: 2 * trap_int(a, b, y, n, function), y_steps)))

    return (d - c) * iter_sum / (2 * n)

def trap_int(a, b, y, n, function):
    # creates the step size
    step = (b - a) / n
    steps = np.arange(a + step, b, step)
    y_iterable = [y for _ in range(len(steps))]
    # adds the sum of the evaluation of the function at each step from a to b
    iter_sum = function(a, y) + function(b, y) + \
               sum(list(map(lambda x, y: 2 * function(x, y), steps, y_iterable)))
    # alters the sum by the range of the bounds and 2n
    return (b - a) * iter_sum / (2 * n)
