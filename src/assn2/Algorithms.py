import sympy as sym
import sys
sym.init_printing(use_latex=True)


def secant(eq, z):
	# sym.plot(eq)
	x_old, x_new = change_x('Enter 2 X bounds close to the root')
	y_old = eq.subs({z: x_old})
	y_new = eq.subs({z: x_new})

	end = False

	while not end:
		slope = (y_new-y_old)/(x_new-x_old)
		# b = y - mx
		b = y_new - slope * x_new
		# x = (y-b)/m
		# find where the straight secant line crosses the x-axis
		x_temp = (y_new - b) / slope
		x_old, y_old = x_new, y_new
		x_new, y_new = x_temp, eq.subs({z: x_temp})

		# ending at maximum precision for float value
		if abs(x_new - x_old) < 0.000000000000001:
			end = True

	return x_new


def false_pos(eq):
	pass


def newton_raphson(eq, z):
	# sym.plot(eq)
	x_old = float(input('Enter an x value close to the root'))
	y = eq.subs({z: x_old})
	deriv = sym.diff(eq, z)

	end = False

	while not end:
		slope = deriv.subs({z: x_old})
		# b = y - mx
		b = y - slope * x_old
		# x = (y-b)/m
		# find where the straight secant line crosses the x-axis
		x_temp = (y - b) / slope

		# ending at maximum precision for float value
		if abs(x_old - x_temp) < 0.000000000000001:
			end = True

		x_old, y = x_temp, eq.subs({z: x_temp})

	return x_old


VALID_INPUT = {
		'X': 'Change the x bounds',
		'Y': 'Change the y bounds',
		'XY': 'Change the x and y bounds',
		'R': 'Replot with the same bounds',
		'Q': 'Quit the Program'
	}


def valid_input():
	user_input = '?'
	print("To change the view of the graph, enter: ")
	while user_input not in VALID_INPUT:
		for i in VALID_INPUT:
			print('|', i, ':', VALID_INPUT[i], '|', sep=" ")
		user_input = input('-->').upper()
	return user_input


def change_x(mes='Enter the new bounds for X'):
	low, high = input(mes + '\n-->').split()
	low, high = float(low), float(high)
	return [low, high]


def change_y(mes='Enter the new bounds for Y'):
	low, high = input(mes + '\n-->').split()
	low, high = float(low), float(high)
	return [low, high]


def graphically(eq):
	sym.plot(eq)

	end = False
	x_lim = [-50, 50]
	y_lim = [-50, 50]

	while not end:
		user_input = valid_input()
		if user_input == 'X':
			x_lim = change_x()
		elif user_input == 'Y':
			y_lim = change_y()
		elif user_input == 'XY':
			x_lim = change_x()
			y_lim = change_y()
		elif user_input == 'Q':
			break
		else:
			continue
			# replot

		sym.plot(eq, block=False, xlim=x_lim, ylim=y_lim)


def get_sign(num):
	if num * -1 > num:
		return False
	else:
		return True


def bisection(eq, x: sym.Symbol, graph=False):
	sym.plot(eq)
	low, high = change_x('Enter X bounds around root')
	y_low = eq.subs({x: low})
	y_high = eq.subs({x: high})

	'''
	True means positive and False is negative.
	This will be used to determine where is the function crosses
	the x axis and changes from positive to negative
	'''
	low_sign = get_sign(y_low)
	high_sign = get_sign(y_high)
	mid = (high + low) / 2
	end = False
	i = 0

	if not low_sign ^ high_sign:
		print("Not a simple root/ Unable to center about a single root")
		end = True

	# stops looping if the root is found or floating point precision becomes significant
	while not end:
		i += 1
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
		if abs(high - low) < 0.000000000000001:
			end = True

		if graph:
			sym.plot(eq, xlim=[low, high])
		print(f"high {high}, low {low}")

	print(f'iteration reached {i} loops')
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
	'M': ['Parse an Equation', make_eq],
	'Q': ['Quit the Program']
}


def print_valid_algorithms():
	print("Enter one of the following algorithms:")
	for i in VALID_ALGORITHMS:
		print(i, ": [", VALID_ALGORITHMS[i][0], "]", sep='')
	return (input("-->")).upper()


def get_algorithm():
	userInput = '?'
	while userInput not in VALID_ALGORITHMS:
		userInput = print_valid_algorithms()
	if userInput == 'Q':
		sys.exit()
	return VALID_ALGORITHMS[userInput][1]

