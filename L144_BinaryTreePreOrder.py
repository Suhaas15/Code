# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # def pre(node):
        #     if not node:
        #         return
            
        #     res.append(node.val)
        #     pre(node.left)
        #     pre(node.right)
        
        # pre(root)
        # return res

        def IterativePre(node):
            if not node:
                return 
                
            stack=[node]
            while stack:
                node=stack.pop()
                res.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        IterativePre(root)
        return res
