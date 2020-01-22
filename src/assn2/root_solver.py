from assn2.Algorithms import *
import sympy as sym


def valid_input():
	user_input = -1
	print("Enter a Error Approximation to stop at: ")
	while 100 > user_input < 0:
		try:
			user_input = float(input('-->:\t'))
		except ValueError:
			valid_input()
	return user_input


if __name__ == "__main__":

	x, y, m = sym.symbols('x y m')

	eq1 = x*x*x*x*x - 10*x*x*x*x + 46*x*x*x - 90*x*x + 85*x - 31
	eq2 = -3*x**3 + 20*x**2 - 20*x - 12
	eq3 = parachutist(9.81, 36, 15, 10, x)
	eq4 = 0.5*x**3 - 4*x**2 + 8*x - 1
	eq5 = -3*x**3 + 20*x**2 - 20*x - 12
	
	func = get_algorithm()
	print(func(eq3, x, valid_input()))
	# print(do_solve(eq3))


