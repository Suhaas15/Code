# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue=deque([root])
        max_sum=float('-inf')
        level=0
        max_level=1

        while queue:
            level_sum=0
            level+=1

            for _ in range(len(queue)):
                node=queue.popleft()
                level_sum+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum>max_sum:
                max_sum=level_sum
                max_level=level
        
        return max_level


