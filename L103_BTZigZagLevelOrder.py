from collections import deque
from typing import List,Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        res=[]
        left_to_right=True

        while q:
            level_size=len(q)
            level_nodes=deque()     #using deque to have fast appends on both ends

            for _ in range(level_size):
                node=q.popleft()
                
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    
            res.append(list(level_nodes))
            left_to_right=not left_to_right
        
        return res

            
