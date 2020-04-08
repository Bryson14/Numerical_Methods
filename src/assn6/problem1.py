from src.assn6.trapazoidal_integration import double_trap_integration
from src.assn6.SimpsonsRules import double_simpson_integration
import numpy as np


def func(x, y):
    return 3 * np.power(x, 2) + 5 * x * y - 6 * y - 7


if __name__ == "__main__":
    a = 0
    b = 10
    c = 0
    d = 15
    print("Give the subsection n, that the function should be evaluated at")
    try:
        n = int(input("-->"))
        assert 1000 >= n > 0
        if n % 2 == 0:  # even
            print(double_simpson_integration(a, b, c, d, n, func))
        else:  # odd
            print(double_simpson_integration(a, b, c, d, n, func))

    except ValueError:
        print("n must be an integer")
    except AssertionError:
        print("n must be between 0 and 1001")
