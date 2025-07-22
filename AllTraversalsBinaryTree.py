class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allTraversals(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
          return [],[],[]

        preorder=[]
        inorder=[]
        postorder=[]

        stack=[(root,1)]

        while stack:
            node,state=stack.pop()

            if state==1:   #preorder
                preorder.append(node.val)
                stack.append((node,2))
                if node.left:
                  stack.append((node.left,1))

            elif state==2:  #inorder
                inorder.append(node.val)
                stack.append((node,3))
                if node.right:
                  stack.append((node.right,1))

            else:  #postorder
                postorder.append(node.val)

        return preorder, inorder, postorder
