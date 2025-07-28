# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res=[]
        
        def rightView(node,level):
            if not node:
                return 
            if len(res)==level:
                res.append(node.val)
            
            rightView(node.right,level+1)
            rightView(node.left,level+1)

            return res
        
        return rightView(root,0)
