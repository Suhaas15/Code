class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=0
        total=0
        place=1

        while n>0:
            d=n%10

            if d!=0:
                num=d*place+num
                place*=10
                total+=d
            n=n//10

        return total*num
