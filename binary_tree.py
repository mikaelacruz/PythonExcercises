"""
Binary Tree
this is all about a binary tree!
we are defining the node class, binary tree class, inserting def, and pre-order traversal
"""
import collections


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



"""Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right"""
class Solution:
    def find_leaves(self, root):
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            level = max(left, right) + 1
            dic[level] += root.val,
            return level

        dic = collections.defaultdict(list)
        helper(root)
        return list(dic.values())
