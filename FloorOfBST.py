class Solution:
    def floor(self, root, x):
      ans=-1

      while root:
        if root.val==x:
          ans=x
          return ans

        if root.val>x:
          root=root.left
        else:
          ans=root.val
          root=root.right

      return ans
