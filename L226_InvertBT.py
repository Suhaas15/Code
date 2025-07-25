from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def swap(node):
        #     if not node:
        #         return 
        #     node.left,node.right=node.right,node.left
        #     left=swap(node.left)
        #     right=swap(node.right)

        # swap(root)
        # return root

        if not root:
            return
        
        q=deque([root])

        while q:
            node=q.popleft()

            node.left,node.right=node.right,node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root
