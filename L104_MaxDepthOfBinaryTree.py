# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def depth(node,count):
        #     if not node:
        #         return count

        #     count+=1
        #     left_depth=depth(node.left,count)
        #     right_depth=depth(node.right,count)

        #     return max(left_depth,right_depth)

        # return depth(root,0)

        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
