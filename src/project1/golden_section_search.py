import sympy as sym
import numpy as np


def change_x(mes):
	low, high = input(mes + '\n--> ').split()
	low, high = float(low), float(high)
	return [low, high]


def golden_section_search(eq, x: sym.Symbol, error_bound, get_minima, graph=False):
	G = 1.6180339887498948													# golden ratio constant
	# sym.plot(eq)
	low, high = change_x('Enter X bounds that bracket the root: ')

	n = int(np.ceil(np.log(error_bound)/(np.log(1/G))))						# finding the number of iterations to achieve error bound
	print(n)
	for i in range(n):
		dx = abs(high - low)
		mid_low = high - dx / G
		mid_low_value = eq.subs({x: mid_low})
		mid_high = low + dx / G
		mid_high_value = eq.subs({x: mid_high})

		if get_minima:														# whether solving for maxima or minima
			if mid_low_value > mid_high_value:
				low = mid_low
			else:
				high = mid_high

		else:
			if mid_low_value < mid_high_value:
				low = mid_low
			else:
				high = mid_high

	if get_minima:
		message = 'minimum'
	else:
		message = 'maximum'

	return f"{message} is approximately {eq.subs({x: low})} and x = {low}"


x = sym.Symbol('x')

func = 2*x+6/x
print(golden_section_search(func, x, 0.00001, True))
