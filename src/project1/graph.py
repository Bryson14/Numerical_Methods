import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
analytic_y = -10 + 19.12080168 * np.exp(0.17321*x) + 10.87919832*np.exp(-0.17321*x)

plt.plot(x,analytic_y, label='Analytic Solution')
plt.show()
plt.waitforbuttonpress()
plt.close('all')