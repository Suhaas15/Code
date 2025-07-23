# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False    
            return check(p.left,q.left) and check(p.right,q.right)
        return check(p,q)
        
        # q=deque([(p,q)])            #BFS
        # while q:
        #     node1,node2=q.popleft()
        #     if not node1 and not node2:
        #         continue
        #     if not node1 or not node2:
        #         return False
        #     if node1.val!=node2.val:
        #         return False
        #     q.append((node1.left,node2.left))
        #     q.append((node1.right,node2.right))
        # return True

        # stack=[(p,q)]           #DFS
        # while stack:
        #     node1,node2=stack.pop()
        #     if not node1 and not node2:
        #         continue
        #     if not node1 or not node2:
        #         return False
        #     if node1.val!=node2.val:
        #         return False
        #     stack.append((node1.right,node2.right))
        #     stack.append((node1.left,node2.left))
        # return True
            
