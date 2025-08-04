# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
          return None

        def helper(root):
            if root.left is None:
              return root.right
            if root.right is None:
              return root.left

            rightChild=root.right
            lastRight=flr(root.left)
            lastRight.right=rightChild
            return root.left

        def flr(root):
          if root.right is None:
              return 
          return flr(root.right)

        if root.val==key:
          return helper(root)

        curr=root
        while root:
            if root.val>key:
                if root.left is not None and root.left.val==key:
                    root.left=helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right is not None and root.right.val==key:
                    root.right=helper(root.right)
                    break
                else:
                  root=root.right
        return curr
