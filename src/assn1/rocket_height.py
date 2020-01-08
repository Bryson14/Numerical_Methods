import sys
import matplotlib.pyplot as plt
import numpy as np


def height(t, sysout=False):
	try:
		t = float(t)
	except ValueError:
		print("Given time t is not a valid number.")
		sys.exit(1)

	if t < 0:
		h = 0
	elif t < 15:
		h = 38.1454 * t + 0.13743 * t * t * t
	elif t < 33:
		h = 1036 + 130.909 * (t - 15) + 6.18425 * (t - 15) * (t - 15) - 0.428 * (t-15)*(t-15)*(t-15)
	else:
		h = 2900 - 62.468 * (t - 33) - 16.9274 * (t - 33) * (t - 33) + 0.41796 * (t - 33) * (t - 33) * (t - 33)

	if sysout:
		print(f"height of the rocket at time {t} is {h} meters")

	return t, h


if __name__ == "__main__":
	if len(sys.argv) > 1:
		t, myH = height(sys.argv[1], True)
		plt.plot(t, myH, "o")

	x = np.arange(50)
	y = np.array([height(t, False)[1] for t in x])

	plt.plot(x, y)
	plt.title("--Rocket Height--")
	plt.xlabel("time (s)")
	plt.ylabel("height (m)")

	plt.show()
