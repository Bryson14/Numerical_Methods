from Algorithms import get_algorithm, parachutist
import sympy as sym


def valid_input():
	user_input = -1
	print("Enter a % error approximation to stop at: ")
	while 100 > user_input < 0:
		try:
			user_input = float(input('-->:\t'))
		except ValueError:
			valid_input()
	return user_input


if __name__ == "__main__":

	x = sym.symbols('x')

	eq1 = x*x*x*x*x - 10*x*x*x*x + 46*x*x*x - 90*x*x + 85*x - 31
	eq2 = -3*x**3 + 20*x**2 - 20*x - 12
	eq3 = parachutist(9.81, 36, 15, 10, x)
	eq4 = 0.5*x**3 - 4*x**2 + 8*x - 1
	eq5 = -3*x**3 + 20*x**2 - 20*x - 12

	eqns = {
		'1': eq1,
		'2': eq2,
		'3': eq3,
		'4': eq4,
		'5': eq5,
	}

	user_input = '?'
	while user_input not in eqns:
		for i in eqns:
			print('|eqn', i , ': ', eqns[i], " | ")
		print('Enter a number between 1 - 5 for the equation to solve')
		user_input = input('-->\t')

	func = get_algorithm()
	print('Root =', func(eqns[user_input], x, valid_input()))


