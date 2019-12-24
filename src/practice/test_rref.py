from unittest import TestCase
import numpy as np
from .rref import get_pivot


class test_get_pivot(TestCase):
	def test_get_pivot(self):
		a = np.array([
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		])
		b = np.array([
			[0, 2, 3],
			[4, 5, 0],
			[7, 8, 0]
		])
		c = np.array([
			[-1, 0, 3],
			[4, 5, 6],
			[7, 8, 9]
		])
		d = np.array([
			[0, 0, 3],
			[4, 0, 6],
			[7, 0, 9]
		])
		e = np.array([
			[0, 0, 3],
			[4, 5, 0],
			[7, 8, 9]
		])

		assert get_pivot(a, 0, 0) == 0
		assert get_pivot(a, 2, 2) == 2
		assert get_pivot(b, 0, 0) == 1
		assert get_pivot(b, 0, 1) == 1
		assert get_pivot(b, 2, 1) == -1
		assert get_pivot(c, 0, 0) == 0
		assert get_pivot(c, 1, 0) == 1
		assert get_pivot(d, 1, 0) == -1
		assert get_pivot(d, 1, 2) == -1
		assert get_pivot(e, 2, 1) == 2
		assert get_pivot(e, 5, 0) == -1


