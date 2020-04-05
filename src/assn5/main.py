import numpy as np
import matplotlib.pyplot as plt
from src.assn5.SimpsonsRules import simpson_integration
from src.assn5.trapazoidal_integration import trap_integration
from src.assn5.adaptive_quad_integration import adap_quad_integration

def hard_func(x):
    return np.power(x, 0.1) * (1.2 - x) * (1 - np.exp(20 * x - 20))


TRUE_VALUE = 0.602298
varying_n_trap = np.concatenate([np.arange(1, 20, .1), np.arange(20, 10000, 50)])
varying_n_simp = np.concatenate([np.arange(1, 20, 1), np.arange(20, 10000, 50)])
varying_tol = np.arange(0.001, .1, .0001)

print('beginning trap')
trap_error = list(map(lambda n: np.abs(TRUE_VALUE - trap_integration(0, 1, n, hard_func)), varying_n_trap))
print('beginning simpson')
simpson_error = list(map(lambda n: np.abs(TRUE_VALUE - simpson_integration(0, 1, n, hard_func)), varying_n_simp))
print('beginning adap')
# adap_quad_error = list(map(lambda tol: np.abs(TRUE_VALUE - adap_quad_integration(0, 1, hard_func, tol)), varying_tol))

plt.plot(varying_n_trap, trap_error, label="Trap Error")
plt.plot(varying_n_simp, simpson_error, label="Simpson Error")
# plt.plot(varying_tol, adap_quad_error, label="Adaptive Quad Error")
plt.title("Error vs Subsections N for Simpsons/ Trapazoidal Function")
plt.legend()
plt.ylabel('Absolute Error')
plt.xlabel('Subsection N')
# plt.ylim(0, 0.07)
# plt.savefig('Trap-Simpson Error_N=10000.png')
plt.show()

