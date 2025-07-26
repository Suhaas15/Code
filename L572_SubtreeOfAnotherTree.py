# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # def solve(p,q):
        #     if not p and not q:
        #         return True
        #     if not p or not q:
        #         return False
        #     if p.val!=q.val:
        #         return False
            
        #     return solve(p.left,q.left) and solve(p.right,q.right)
        # if not root:
        #     return False
        # if solve(root,subRoot):
        #     return True
        # return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        def serialize(node):
            res=[]

            def dfs(n):
                if not n:
                    res.append("#")
                    return 
                res.append(","+str(n.val))
                dfs(n.left)
                dfs(n.right)
            dfs(node)
            return ",".join(res)
        
        root_serial=serialize(root)
        sub_serial=serialize(subRoot)

        return sub_serial in root_serial

