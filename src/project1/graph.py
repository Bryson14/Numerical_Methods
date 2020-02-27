import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
analytic_y = -10 + 19.12080168 * np.exp(0.17321*x) + 10.87919832*np.exp(-0.17321*x)

x_2 = np.arange(0, 11, 1)
numerical_y = np.array([20, 21.89739354, 24.75170889, 28.6485755, 33.70489938, 40.07237024, 47.9420122,
 57.54991453, 69.1843143, 83.1942435, 100])


plt.plot(x,analytic_y, label='Analytic Solution')
for i in range(x_2.size -1 ):
    plt.plot(x_2[i], numerical_y[i], '-x')
plt.plot(x_2[-1], numerical_y[-1], '-x', label='Numerical Solutions')
plt.xlabel('X (m)')
plt.ylabel('Temperature (Celsius)')
plt.title('Analytic and Numerical Temperature Solutions')
plt.legend()
plt.show()
