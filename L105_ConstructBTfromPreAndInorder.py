# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map={val: i for i, val in enumerate(inorder)}
        self.index=0

        def helper(start,end):
            if start>end:
                return None
            
            root_val=preorder[self.index]
            self.index+=1
            root=TreeNode(root_val)

            mid=idx_map[root_val]
            root.left=helper(start,mid-1)
            root.right=helper(mid+1,end)
            return root
        
        return helper(0,len(inorder)-1)
