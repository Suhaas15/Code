class Solution:
    def removeZeros(self, n: int) -> int:
        digits=[]
        while n>0:
             digit=n%10
             n=n//10
             digits.append(digit)

        digits = [digit for digit in digits if digit != 0]

        number=0
        for digit in reversed(digits):
            number = number * 10 + digit

        return number
