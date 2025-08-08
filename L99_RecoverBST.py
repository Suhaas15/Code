# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.prev=self.first=self.second=None            #recursive

        # def inorder(node):
        #     if not node:
        #         return

        #     inorder(node.left)
        #     if self.prev and self.prev.val>node.val:
        #         if self.first:
        #             self.first=self.prev
        #         self.second=node
        #     self.prev=node
        #     inorder(node.right)

        # inorder(root)
        # self.first.val,self.second.val=self.second.val,self.first.val

        first=second=prev=None
        curr=root

        while curr:
            if curr.left:
                # Find the predecessor
                pre = curr.left
                while pre.right and pre.right != current:
                    pre = pre.right

                if not pre.right:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    if prev and prev.val > current.val:
                        if not first:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
            else:
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right

        if first and second:
            first.val,second.val=second.val,first.val
