# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0

            left=check(node.left)
            if left==-1:
                return -1

            right=check(node.right)
            if right==-1:
                return -1
            
            if abs(left-right)>1:
                return -1
            
            return 1+max(left,right)
        
        return check(root)!=-1
            
