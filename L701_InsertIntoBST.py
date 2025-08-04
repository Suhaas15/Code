# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        # curr=root           #iterative method
        # while True:
        #     if curr.val>val:
        #         if curr.left is None:
        #             curr.left=TreeNode(val)
        #             break
        #         else:
        #             curr=curr.left
        #     else:
        #         if curr.right is None:
        #             curr.right=TreeNode(val)
        #             break
        #         else:
        #             curr=curr.right
        
        # return root

        if val<root.val:                #recursive method
            root.left=self.insertIntoBST(root.left,val)
        else:
            root.right=self.insertIntoBST(root.right,val)
        
        return root
        
        
