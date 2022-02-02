"""
Binary Tree
this is all about a binary tree!
we are defining the node class, binary tree class, inserting def, and pre-order traversal
"""


class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		elif value > self.value:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)
		else:
			self.value = value




class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def preorder_print(self, root, traversal):
		if root:
			traversal += (str(root.value) + "-")
			traversal = self.preorder_print(root.left, traversal)
			traversal = self.preorder_print(root.right, traversal)
		return traversal

	def inorder_print(self, root, traversal):
		if root:
			traversal = self.inorder_print(root.left, traversal)
			traversal += (str(root.value) + "-")
			traversal = self.inorder_print(root.right, traversal)
		return traversal

	def postorder_print(self, root, traversal):
		if root:
			traversal = self.postorder_print(root.left, traversal)
			traversal = self.postorder_print(root.right, traversal)
			traversal += (str(root.value))
		return traversal

	# you would call with tree_name.print_tree("traversal_type")


	def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder_print(self.root, "")
		elif traversal_type == "inorder":
			return self.inorder_print(self.root, "")
		elif traversal_type == "postorder":
			return self.postorder_print(self.root, "")
		else:
			print("Traversal type" + str(traversal_type) + "is not supported")
			return False
