# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_bst_size=0

        def dfs(node):
            # Returns: (is_bst, size, min_val, max_val)
            if not node:
                return (True,0,float('inf'),float('-inf'))

            left_is_bst,left_size,left_min,left_max=dfs(node.left)
            right_is_bst,right_size,right_min,right_max=dfs(node.right)

            if left_is_bst and right_is_bst and left_max<node.val<right_min:
                curr_size=left_size+1+right_size
                self.max_bst_size=max(self.max_bst_size,curr_size)
                return (True,curr_size,min(node.val,left_min),max(node.val,right_max))
            else:
                return (False,0,0,0)

        dfs(root)
        return self.max_bst_size
            
