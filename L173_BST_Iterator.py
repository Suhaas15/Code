# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):        #recursive
        self.i=0                                  
        self.vals=[]
        self._inorder(root)

    def next(self) -> int:
        self.i+=1
        return self.vals[self.i-1]

    def hasNext(self) -> bool:
        return self.i<len(self.vals)

    def _inorder(self, root: TreeNode | None) -> None:
        if not root:
            return
        _inorder(root.left)
        self.vals.append(root.val)
        _inorder(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):        #iterative
        self.stack=[]
        self.pushLeftUntilNull(root)

    def next(self) -> int:
        root=self.stack.pop()
        self.pushLeftUntilNull(root.right)
        return root.val

    def hasNext(self) -> bool:
        return bool(self.stack)

    def pushLeftUntilNull(self, root: TreeNode | None) -> None:
        if not root:
            return
        _inorder(root.left)
        self.vals.append(root.val)
        _inorder(root.right)
