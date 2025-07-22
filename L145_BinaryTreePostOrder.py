# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        # def post(node):
        #     if not node:
        #         return 
            
        #     post(node.left)
        #     post(node.right)
        #     res.append(node.val)
        
        # post(root)
        # return res

        # def IterativePostOrderWith2Stacks(node):
        #     if not node:
        #         return []
                
        #     stack1=[root]
        #     stack2=[]
    
        #     while stack1:
        #         node=stack1.pop()
        #         stack2.append(node)
    
        #         if node.left:
        #             stack1.append(node.left)
        #         if node.right:
        #             stack1.append(node.right)
    
        #     while stack2:
        #         node=stack2.pop()
        #         res.append(node.val)
                
        # ItertativePreOrderWith2Stacks(root)
        # return res

        def IterativePostWith1Stack(node):
            if not node:
                return []

            stack=[]
            current=node
            last_visited=None

            while stack or current:
                while current:
                    stack.append(current)
                    current=current.left

                peek_node=stack[-1]

                if peek_node.right and last_visited!=peek_node.right:
                    current=peak_node.right
                else:
                    res.append(peek_node.val)
                    last_visited=current
                    
        IterativePostWith1Stack(root)
        return res
