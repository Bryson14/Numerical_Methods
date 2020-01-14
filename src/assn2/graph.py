import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
sym.init_printing(use_latex=True)
import sys
import re


def secant(eq):
	pass


def false_pos(eq):
	pass


def newton_raphson(eq):
	pass


def graphically(eq):
	end = False
	xlim = [-50, 50]
	ylim = [-50 , 50]
	while not end:
		sym.plot(eq, block=False, xlim=xlim, ylim=ylim)
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


def bisection(eq, graph=False):
	sym.plot(eq)
	xlim = [0.0,0.0]
	xlim[0], xlim[1] = (input("Enter the range of numbers for the X BOUNDS to examine separated by a space: ")).split()
	xlim[0], xlim[1] = float(xlim[0]), float(xlim[1])

	low = xlim[0]
	high = xlim[1]
	y_low = eq.subs({x: low})
	y_high = eq.subs({x: high})

	'''
	True means positive and False is negative. This will be used to determine where is the function crosses
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
			y_high = y_mid
		elif mid_sign ^ high_sign:
			low = mid
			y_low = y_mid
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
	# sym = []
	#
	# terms = re.split('\+|-|\*|/', arg)
	# print(terms)
	pass


def do_solve(eq):
	sols = sym.solve(eq)
	return[sym.N(sol) for sol in sols]


if __name__ == "__main__":

	x, y = sym.symbols('x y')

	eq1 = x*x*x*x*x - 10*x*x*x*x + 46*x*x*x - 90*x*x + 85*x - 31
	eq2 = -3*x**3 + 20*x**2 - 20*x - 12
	eq4 = 0.5*x**3 - 4*x**2 + 8*x - 1
	eq5 = -3*x**3 + 20*x**2 - 20*x - 12

	# roots = sym.solve(eq1, x)
	# print(roots)
	
	# graphically(eq1)
	print(bisection(eq1, graph=False))
	print(do_solve(eq1))



