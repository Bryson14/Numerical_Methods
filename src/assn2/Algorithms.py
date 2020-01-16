import sympy as sym
import sys
sym.init_printing(use_latex=True)


def secant(eq):
	pass


def false_pos(eq):
	pass


def newton_raphson(eq):
	pass


VALID_INPUT = {
		'X': ['Change the x bounds'],
		'Y': ['Change the y bounds'],
		'XY': ['Change the x and y bounds'],
		'R': ['Replot with the same bounds'],
		'Q': ['Quit the Program']
	}

def graphically(eq):
	end = False
	xlim = [-50, 50]
	ylim = [-50 , 50]


	def valid_input():
		pass

	def change_x(inpt: str):
		xlim[0], xlim[1] = inpt.split()
		xlim[0], xlim[1] = float(xlim[0]), float(xlim[1])

	def change_y(inpt: str):
		ylim[0], ylim[1] = inpt.split()
		ylim[0], ylim[1] = float(ylim[0]), float(ylim[1])

	while not end:
		sym.plot(eq, block=False, xlim=xlim, ylim=ylim)

		valid_input()
		change = input('to change the y bounds, enter y. To change the x bounds, enter x: ')
		if change == 'y':
			ylim[0], ylim[1] = (input("Enter the range of numbers to examine separated by a space: ")).split()
			ylim[0], ylim[1] = float(ylim[0]), float(ylim[1])
		elif change == 'x':
			xlim[0], xlim[1] = (input("Enter the range of numbers to examine separated by a space: ")).split()
			xlim[0], xlim[1] = float(xlim[0]), float(xlim[1])
		elif change == 'xy' or change == 'x y':
			xlim[0], xlim[1] = (input("Enter the range of numbers for X BOUNDS to examine separated by a space: ")).split()
			xlim[0], xlim[1] = float(xlim[0]), float(xlim[1])
			ylim[0], ylim[1] = (input("Enter the range of numbers for Y BOUNDS to examine separated by a space: ")).split()
			ylim[0], ylim[1] = float(ylim[0]), float(ylim[1])
		else:
			end = True


def get_sign(num):
	if num * -1 > num:
		return False
	else:
		return True


def bisection(eq, x, graph=False):
	sym.plot(eq)
	xlim = [0.0, 0.0]
	xlim[0], xlim[1] = (input("Enter the range of numbers for the X BOUNDS to examine separated by a space: ")).split()
	xlim[0], xlim[1] = float(xlim[0]), float(xlim[1])

	low = xlim[0]
	high = xlim[1]
	y_low = eq.subs({x: low})
	y_high = eq.subs({x: high})

	'''
	True means positive and False is negative.
	This will be used to determine where is the function crosses
	the x axis and changes from positive to negative
	'''
	low_sign = get_sign(y_low)
	high_sign = get_sign(y_high)
	if not low_sign ^ high_sign:
		print("Not a simple root")
		sys.exit()
	mid = (high + low) / 2
	end = False

	# stops looping if the root is found or floating point precision becomes significant
	while not end:
		mid = (high + low) / 2
		y_mid = eq.subs({x: mid})
		mid_sign = get_sign(y_mid)

		# if mid and low are on other sides of the x axis
		if mid_sign ^ low_sign:
			high = mid
		elif mid_sign ^ high_sign:
			low = mid
		else:
			end = True

		# 1 x 10^-15 to max out floating point precision
		if abs((high - low)) < 0.00000000000001:
			end = True

		if graph:
			sym.plot(eq, xlim=[low,high])
		print(f"high {high}, low {low}")

	return mid


def make_eq(arg: str):
	eq = None
	return eq


def do_solve(eq):
	sols = sym.solve(eq)
	return[sym.N(sol) for sol in sols]


def parachutist(g, v, c, t, m):
	eq = g * m * (1 - sym.exp(- c * t / m)) / c
	return eq


VALID_ALGORITHMS = {
	'S': ['Solve with Sympy', do_solve],
	'B': ['Bisection Method', bisection],
	'P': ['Make Equation for Parachutist Problem', parachutist],
	'G': ['Graphic Method', graphically],
	'F': ['False Position Method', false_pos],
	'N': ['Newton-Raphson Method', newton_raphson],
	'C': ['Secant Method', secant],
	'M': ['Parse an Equation', make_eq]
}


def print_valid_algorithms():
	print("Enter one of the following algorithms:")
	for i in VALID_ALGORITHMS:
		print(i, ": [", VALID_ALGORITHMS[i][0], "]", sep='')
	return (input("-->")).upper()


def algorithm_menu():
	print("what algorithm would you like to use?")
	user_input = '?'
	while user_input not in VALID_ALGORITHMS:
		user_input = print_valid_algorithms()
	n = int(input("Enter the integer input for the algorithm:"))
	print()
	print("return value of", VALID_ALGORITHMS[user_input][0], "with n =", n, ":", VALID_ALGORITHMS[user_input][1](n))


def get_algorithm():
	userInput = '?'
	while userInput not in VALID_ALGORITHMS:
		userInput = print_valid_algorithms()
	return VALID_ALGORITHMS[userInput][1]
