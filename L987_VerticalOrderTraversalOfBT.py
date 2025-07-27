from collections import defaultdict,deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeMap = defaultdict(lambda: defaultdict(list))
        q=deque([(root,0,0)])

        while q:
            node,x,y=q.popleft()
            nodeMap[x][y].append(node.val)

            if node.left:
                q.append((node.left,x-1,y+1))
            if node.right:
                q.append((node.right,x+1,y+1))
        
        res=[]

        for x in sorted(nodeMap.keys()):
            col=[]
            for y in sorted(nodeMap[x].keys()):
                col.extend(sorted(nodeMap[x][y]))
            res.append(col)
        
        return res
