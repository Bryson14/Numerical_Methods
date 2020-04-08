from src.assn6.trapazoidal_integration import double_trap_integration
from src.assn6.SimpsonsRules import double_simpson_integration
import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    return np.power(x, 2) - 3 * np.power(y, 2) + x * y + 72


if __name__ == "__main__":
    a = -2
    b = 2
    c = 0
    d = 4
    TRUE_ANS = 57.333333333333333
    calculated_ans = []
    for n in range(1, 6):
        if n % 2 == 0:  # even
            ans = double_simpson_integration(a, b, c, d, n, func) / ((b-a)*(d-c))
        else:  # odd
            ans = double_trap_integration(a, b, c, d, n, func) / ((b-a)*(d-c))

        calculated_ans.append(100 * abs(ans - TRUE_ANS) / TRUE_ANS)

    plt.plot(np.arange(1, 6, 1), calculated_ans, label="Percent Relative Error")
    plt.xticks(np.arange(0, 7, 1))
    plt.title("Relative Percent Error vs Subsections n")
    plt.xlabel("n")
    plt.ylabel("Percent Error %")
    # plt.savefig("Average Temp Error more n.png")
    plt.show()
