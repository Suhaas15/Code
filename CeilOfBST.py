# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the ceiling of
    # a key in a Binary Search Tree (BST)
    def findCeil(self, root, key):
      ceil=-1

      while root:
        if root.val==key:
          ceil=root.val
          return ceil

        if root.val>key:
          root=root.right
        else:
          ceil=root.val
          root=root.left

      return ceil
