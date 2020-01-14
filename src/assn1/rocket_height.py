import sys
import matplotlib.pyplot as plt
import numpy as np


def height(t, sys_out=False):
	# throws exception for input that is not a float type
	try:
		if not isinstance(t, float):
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

	if sys_out:
		print(f"height of the rocket at time {t} is {h} meters")

	# returns float t and float h for convenience
	return t, h


# enables cmd line interface
# USAGE python rocket_height.py [TIME_IN_FIGHT]
if __name__ == "__main__":
	# creates the graph
	x = np.arange(48, dtype='float')
	y = np.array([height(t)[1] for t in x])
	plt.plot(x, y)

	if len(sys.argv) > 1:
		# adds point to plot and logs out to console the height at a given time
		time, myH = height(sys.argv[1], True)
		plt.plot(time, myH, "o")

	# labels graph
	plt.title("--Rocket Height--")
	plt.xlabel("time (s)")
	plt.ylabel("height (m)")

	# show graph, press 'q' to end
	plt.show()
