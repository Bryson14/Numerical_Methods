class Tree:

	def __init__(self, inOrderTrav : [int]):
		self.__treeName = "tree"
		self.__root = None
		self.__curr = None
		self.__inOrder = inOrderTrav
		self.build_tree()

	def build_tree(self):
		for value in self.__inOrder:
			self.__root = self.insert(self.__root, value, None)

	def insert(self, root, value, parent):

		if root is None:
			return Node(value, parent)

		elif root.value <= value:
			root.right = self.insert(root.right, value, root)
		else:
			root.left = self.insert(root.left, value, root)

		return root

	def depth(self):
		return self.get_depth(self.__root, 0)

	def get_depth(self, node, level):
		if node is None:
			return level
		else:
			return max(self.get_depth(node.left, level + 1), self.get_depth(node.right, level + 1))

	def to_string(self):
		for i in range(self.depth()):
			self.to_string_recur(self.__root, i, 0)
			print()

	def to_string_recur(self, node, height, level):
		if node is None:
			print("   ", end="")
		elif level == height:
			print(node.value , "   ", end="")
		else:
			self.to_string_recur(node.left, height, level + 1)
			self.to_string_recur(node.right, height, level + 1)

	def pop(self):
		root = self.__root.value
		right = self.__root.right
		left = self.__root.left

		if self.__root.right is None:
			self.__root = self.largest(self.__root.left)
		else:
			self.__root = self.smallest(self.__root.right)

		self.__root.left = left
		self.__root.left.parent = self.__root
		self.__root.right = right
		self.__root.right.parent = self.__root

		if self.__root.parent.left.value == self.__root.value:
			self.__root.parent.left = None
		else:
			self.__root.parent.right = None

		self.__root.parent = None
		return root

	def smallest(self, node):
		if node is None or node.left is None:
			return node
		else:
			return self.smallest(node.left)

	def largest(self, node):
		if node is None or node.right is None:
			return node
		else:
			return self.smallest(node.right)



class Node:
	def __init__(self, value: int, parent):
		self.value = value
		self.parent = parent
		self.left = None
		self.right = None


inOrderTraverse = [50, 30, 70, 10, 40, 60, 90, 20, 80]
my_tree = Tree(inOrderTraverse)
print(my_tree.pop(), ": popped")
print(my_tree.to_string())

