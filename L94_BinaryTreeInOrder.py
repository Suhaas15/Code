# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        # def inOrder(node):
        #     if not node:
        #         return
            
        #     inOrder(node.left)
        #     res.append(node.val)
        #     inOrder(node.right)
        
        # inOrder(root)
        # return res 

        def IterativeIn(node):
            stack=[node]
            current=root

            while stack or current:
                while current:
                    stack.append(current)
                    current=current.left

                current=stack.pop()
                res.append(current)

                current=current.right
        IterativeIn(root)
        return res
