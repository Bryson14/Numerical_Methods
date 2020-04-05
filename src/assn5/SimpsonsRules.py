import numpy as np
import matplotlib.pyplot as plt

def function(x):
    y = 3 * np.power(x, 2) + 5*x - 7
    return y


def trap_integration(a, b, n):
    # creates the step size
    step = (b - a) / n
    # adds the sum of the evaluation of the function at each step from a to b
    iter_sum = function(a) + function(b) + sum(list(map(lambda x: 2 * function(x), np.arange(a + step, b, step))))
    # alters the sum by the range of the bounds and 2n
    return (b - a) * iter_sum / (2 * n)

def simpson_third_integration(a, b, n):
    step = (b - a) / n
    even_sum = 0
    odd_sum = 0
    all_x = np.arange(a + step, b, step)
    for i in range(len(all_x)):
        if i == 0 or i % 2 == 0:  # even
            even_sum += 2 * function(all_x[i])
        else:  # odd
            odd_sum += 4 * function(all_x[i])

    return (function(a) + even_sum + odd_sum + function(b)) / (3*n)

def simpson_three_eighths_integration(a, b, n):
    step = (b - a) / n
    return (b - a) * (function(a) + 3*function(a+step) + 3 * function(a + 2 * step) + function(b)) / (8)


def simpson_integration(a, b, n):
    # if n == 1, use trap rule
    if n == 1:
        return trap_integration(a, b, 1)
    # if n is even, use simpson 1/3 rule
    elif n % 2 == 0:
        return simpson_third_integration(a, b, n)

    # if n is odd, use simpson 1/3 for all but the last three sub-interval, which uses simpson 3/8 rule
    elif n >= 3:
        step = (b - a) / n
        return simpson_third_integration(a, b - 3 * step, n - 3) \
               + simpson_three_eighths_integration(b - 3 * step, step, 3)

    else:
        print(f"n, {n}, is weird")
        return "Error"


print(simpson_integration(0 , 5, 100))