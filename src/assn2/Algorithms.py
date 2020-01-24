import sympy as sym
import sys
sym.init_printing(use_latex=True)


def get_sign(num):
	if num * -1 > num:
		return False
	else:
		return True


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
	low, high = input(mes + '\n--> ').split()
	low, high = float(low), float(high)
	return [low, high]


def change_y(mes='Enter the new bounds for Y'):
	low, high = input(mes + '\n-->').split()
	low, high = float(low), float(high)
	return [low, high]


def secant(eq, z, error_bound):
	# x_temp = x(i+1) , x_new = x(i), x_old = x(i-1)
	sym.plot(eq)
	x_old, x_new = change_x('Enter 2 X bounds close to the root: ')

	end = False

	while not end:
		y_old = eq.subs({z: x_old})
		y_new = eq.subs({z: x_new})

		x_temp = x_new - (y_new * (x_old - x_new)) / (y_old - y_new)

		x_old, y_old = x_new, y_new
		x_new, y_new = x_temp, eq.subs({z: x_temp})

		# ending at the user specified percent error
		error_approx = 100 * (x_new - x_old) / x_new
		if abs(error_approx) < error_bound:
			end = True
			print(f"approximate error is {abs(error_approx)} %")

	return x_new


def false_pos(eq, z, error_bound):
	# x_temp = x(i+1) , x_new = x(i), x_old = x(i-1)
	sym.plot(eq)
	x_old, x_new = change_x('Enter 2 X bounds that bracket to the root: ')
	y_old = eq.subs({z: x_old})
	y_new = eq.subs({z: x_new})

	end = False
	i = 0

	while not end:
		i += 1
		old_sign = get_sign(y_old)
		new_sign = get_sign(y_new)

		if not (old_sign ^ new_sign):
			print(f"Bounds {x_old} and {x_new} don't bracket the root")
			sys.exit()

		x_temp = x_new - (y_new * (x_old - x_new)) / (y_old - y_new)
		y_temp = eq.subs({z: x_temp})
		temp_sign = get_sign(y_temp)

		# the only difference between secant and false position method is that

		# if temp and old are on other sides of the x axis, the Old stays the same and temp becomes new
		if old_sign ^ temp_sign:
			error_approx = 100 * (x_temp - x_new) / x_temp
			x_new, y_new = x_temp, y_temp

		# if new and temp are on opposite side of the x axis, new become the old, and temp becomes new
		elif new_sign ^ temp_sign:
			error_approx = 100 * (x_temp - x_old) / x_temp
			x_old, y_old = x_new, y_new
			x_new, y_new = x_temp, y_temp

		# bounds don't bracket the root
		else:
			end = True
			print("Not a simple root/ Unable to center about a single root")
			error_approx = 0.0

		# print(f"x_i = {x_new}, and x_i-1 = {x_old}, iterations = {i}")

		# ending at the user specified percent error
		if abs(error_approx) < error_bound:
			end = True
			print(f"approximate error is {abs(error_approx)} % \n iterations = {i}")

	return x_new


def newton_raphson(eq, z, error_bound):
	# sym.plot(eq)
	x_old = float(input('Enter an x value close to the root: '))
	y = eq.subs({z: x_old})
	deriv = sym.diff(eq, z)

	end = False

	while not end:
		slope = deriv.subs({z: x_old})
		x_temp = x_old - y/slope

		# ending at the user specified percent error
		error_approx = 100 * (x_temp - x_old) / x_temp
		if abs(error_approx) < error_bound:
			end = True

		x_old, y = x_temp, eq.subs({z: x_temp})

	print(f"approximate Error is {abs(error_approx)} %")
	return x_old


def graphically(eq, z, error_bound):
	sym.plot(eq)

	end = False
	x_lim = [-30, 30]
	y_lim = [-30, 30]

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


def bisection(eq, x: sym.Symbol, error_bound, graph=False):
	sym.plot(eq)
	low, high = change_x('Enter X bounds that bracket the root: ')
	y_low = eq.subs({x: low})
	y_high = eq.subs({x: high})

	# bounds are symmetric about the x axis, then add a small amount to avoid divide by zero error
	if low * -1 == high:
		low -= 0.0000001

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
			error_approx = 100 * (low - mid) / mid
		elif mid_sign ^ high_sign:
			low = mid
			error_approx = 100 * (high - mid) / mid
		else:
			end = True
			error_approx = 0.0

		# 1 x 10^-15 to max out floating point precision

		if abs(error_approx) < error_bound:
			end = True

		if graph:
			sym.plot(eq, xlim=[low, high])
		# print(f"high {high}, low {low}")

	print(f'iteration reached {i} loops. Approximate Error is {error_approx}%')
	return mid


def do_solve(eq, x, error):
	sols = sym.solve(eq)
	return[sym.N(sol) for sol in sols]


def parachutist(g, v, c, t, m):
	eq = (g * m * (1 - sym.exp(- c * t / m)) / c) - v
	return eq


VALID_ALGORITHMS = {
	'B': ['Bisection Method', bisection],
	'G': ['Graphic Method', graphically],
	'F': ['False Position Method', false_pos],
	'N': ['Newton-Raphson Method', newton_raphson],
	'S': ['Secant Method', secant],
	'P': ['Solve with Sympy', do_solve],
	'Q': ['Quit the Program']
}


def print_valid_algorithms():
	print("Enter one of the following algorithms:")
	for i in VALID_ALGORITHMS:
		print(i, ": [", VALID_ALGORITHMS[i][0], "]", sep='')
	return (input("-->")).upper()


def get_algorithm():
	user_input = '?'
	while user_input not in VALID_ALGORITHMS:
		user_input = print_valid_algorithms()
	if user_input == 'Q':
		sys.exit()
	return VALID_ALGORITHMS[user_input][1]

