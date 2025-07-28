from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def topView(self, root):
        res = []
        if not root:
            return res

        q = deque([(root, 0)])     # (node, horizontal distance)
        mpp = {}                   # map of line -> first node at that line

        while q:
            node, line = q.popleft()

            if line not in mpp:
                mpp[line] = node.val

            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))

        for line in sorted(mpp.keys()):
            res.append(mpp[line])

        return res
