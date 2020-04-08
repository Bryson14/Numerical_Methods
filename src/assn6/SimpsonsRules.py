import numpy as np
from src.assn5.trapazoidal_integration import trap_integration

# simpson's 1/3 integration rule for even amounts of subsets
def simpson_third_integration(a, b, y, n, function):
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
            iter_sum += 4 * function(all_x[i], y)
        else:  # odd
            iter_sum += 2 * function(all_x[i], y)

    return (b - a) * (function(a, y) + iter_sum + function(b, y)) / (3*n)

def double_simpson_integration(a, b, c, d, n, function):
    if n <= 0:
        return 0.0
    step = (d - c) / n
    iter_sum = 0
    all_y = np.arange(c + step, d, step)
    '''
    In the mathematical formula, 4f(xi) is for x=1,3,5,... and 2f(xi) for x=2,4,6
    However, this means that first item in all_x is x_1 in the mathematical formula. So in the program
    the even terms are multiplied by 4 and the odd terms are multiplied by 2
    '''
    for i in range(len(all_y)):
        if i == 0 or i % 2 == 0:  # even
            iter_sum += 4 * simpson_third_integration(a, b, all_y[i], n, function)
        else:  # odd
            iter_sum += 2 * simpson_third_integration(a, b, all_y[i], n, function)

    return (d - c) * (simpson_third_integration(a, b, c, n, function) + iter_sum +
                      simpson_third_integration(a, b, d, n, function)) / (3*n)
