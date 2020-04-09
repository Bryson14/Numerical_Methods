import numpy as np
import matplotlib.pyplot as plt
'''
y_x+1 = y_x + h * f(t_x, y_x)
'''
def euler(var1, var2, step):

    current = var2
    variables_1 = [current]
    times = [0]
    variables_2 = [var1]
    index = 0
    while current > 0:  # hasn't hit the ground yet
        if index % (1/step) == 0:
            print(index)

        variables_2.append(variables_2[index] + function2(variables_2[index]) * step)
        variables_1.append(variables_1[index] + function1(variables_2[index]) * step)
        times.append(index * step)
        current = variables_1[index + 1]
        index += 1

    return times, variables_1, variables_2

'''
ODE representing a differntial equation
'''
def function2(v):
    return FUNCTION


'''
ODE representing a differntial equation
'''
def function1(v):
    return FUNCTION


'''
Runge-Kutta Method is a better version basically of Euler's Method.
 t takes four different approximations at each step, then makes the next step an average of the four approximations.

'''
def runge_kutta(var1, var2, step):
    current = var2
    variables_1 = [current]
    times = [0]
    variables_2 = [var1]
    index = 0

    while current > 0:  # hasn't hit the ground yet

        approx_a1 = function1(variables_2[index])
        approx_b1 = function2(variables_2[index])

        approx_a2 = function1(variables_2[index] + 0.5 * step * approx_b1)
        approx_b2 = function2(variables_2[index] + 0.5 * step * approx_b1)

        approx_a3 = function1(variables_2[index] + 0.5 * step * approx_b2)
        approx_b3 = function2(variables_2[index] + 0.5 * step * approx_b2)

        approx_a4 = function1(variables_2[index] + step * approx_b3)
        approx_b4 = function2(variables_2[index] + step * approx_b3)

        variables_2.append(variables_2[index] + (approx_b1 + 2*approx_b2 + 2*approx_b3 + approx_b4) * step / 6)
        variables_1.append(variables_1[index] + (approx_a1 + 2*approx_a2 + 2*approx_a3 + approx_a4) * step / 6)
        times.append(index * step)
        current = variables_1[index + 1]
        index += 1

    return times, variables_1, variables_2
