class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        
        left,right=0,x

        while left+1<right:
            mid=(left+right)//2
            sq=mid*mid

            if sq==x:
                return mid
            elif sq>x:
                right=mid
            else:
                left=mid
        
        return left
