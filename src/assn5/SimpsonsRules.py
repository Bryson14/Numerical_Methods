import numpy as np
from src.assn5.trapazoidal_integration import trap_integration

# the function that is being integrated
def func(x):
    return 3 * np.power(x, 2) + 5*x - 7

# simpson's 1/3 integration rule for even amounts of subsets
def simpson_third_integration(a, b, n, function):
    if n <= 0:
        return 0.0
    step = (b - a) / n
    iter_sum = 0
    all_x = np.arange(a + step, b, step)
    '''
    In the mathematical formula, 4f(xi) is for x=1,3,5,... and 2f(xi) for x=2,4,6
    However, this means that first item in all_x is x_1 in the mathematical formula. So in the program
    the even terms are multiplied by 4 and the odd terms are multiplied by 2
    '''
    for i in range(len(all_x)):
        if i == 0 or i % 2 == 0:  # even
            iter_sum += 4 * function(all_x[i])
        else:  # odd
            iter_sum += 2 * function(all_x[i])

    return (b - a) * (function(a) + iter_sum + function(b)) / (3*n)

# simpson's 3/8 integration rule for the last 3 sub sections
def simpson_three_eighths_integration(a, b, n, function):
    step = (b - a) / n
    return (b - a) * (function(a) + 3*function(a+step) + 3 * function(a + 2 * step) + function(b)) / 8

# driver code for deciding which rule to use
def simpson_integration(a, b, n, function):
    # if n == 1, use trap rule
    if n == 1:
        return trap_integration(a, b, 1, function)
    # if n is even, use simpson 1/3 rule
    elif n % 2 == 0:
        return simpson_third_integration(a, b, n, function)

    # if n is odd, use simpson 1/3 for all but the last three sub-interval, which uses simpson 3/8 rule
    elif n >= 3:
        step = (b - a) / n
        return simpson_third_integration(a, b - 3 * step, n - 3, function) \
               + simpson_three_eighths_integration(b - 3 * step, b, 3, function)

    else:
        print(f"n, {n}, is weird")
        return "Error"
