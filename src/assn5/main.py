import numpy as np
from src.assn5.SimpsonsRules import simpson_integration
from src.assn5.trapazoidal_integration import trap_integration
from src.assn5.adaptive_quad_integration import adap_quad_integration

def hard_func(x):
    return np.power(x, 0.1) * (1.2 - x) * (1 - np.exp(20 * x - 20))


print(simpson_integration(0, 1, 10000, hard_func))
