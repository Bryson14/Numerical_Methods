from tkinter import Tk, Canvas, Label
import numpy as np


class BlackWhiteGrid:
	def __init__(self, root=None):
		self.root = root
		self.arr = None
		self.canvas = None
		self.BLACK = "#000000"
		self.WHITE = "#ffffff"

	def read_array(self, arr):
		self.arr = arr
		self.canvas = Canvas(self.root)
		print(arr.shape)
		height, width = arr.shape[0], arr.shape[1]
		winHeight, winWidth = 600, 900
		square_width, square_height = winWidth // width//2, winHeight // height//2

		for i in range(height):
			for j in range(width):
				val = self.arr[i][j]
				if val == 0:
					Label(self.root, text="  0  ", bg=self.BLACK, fg =self.WHITE).grid(row=i, column = j)
				else:
					Label(self.root, text="  1   ", fg=self.BLACK, bg=self.WHITE).grid(row=i, column=j)


def main():

	root = Tk()
	grid = BlackWhiteGrid(root)

	a = np.random.random(500)*2//1
	a = np.reshape(a, (25, 20))

	grid.read_array(a)

	root.geometry("1000x700+275+75")
	root.mainloop()


if __name__ == '__main__':
	main()
