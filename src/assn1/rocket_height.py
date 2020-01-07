import sys


def height(t):
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

	print(f"height of the rocket at time {t} is {h} meters")


if __name__ == "__main__":
	height(sys.argv[1])
