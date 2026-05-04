class Solution:
    def rotatedDigits(self, n: int) -> int:
        def check(num):
            different = False
            while num:
                digit = num % 10
                num //= 10
                if digit in (3, 4, 7):
                    return False
                if digit in (2, 5, 6, 9):
                    different = True
            return different  

        count=0
        for i in range(1, n + 1):
            if check(i):
                count+=1
        return count
