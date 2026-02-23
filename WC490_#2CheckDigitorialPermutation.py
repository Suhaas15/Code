class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        factorials=[1]
        for digit in range(1,10):
            factorials.append(factorials[-1]*digit)
        
        digits_sum = sum(factorials[digit] for digit in map(int,str(n)))
        return Counter(str(digits_sum)) == Counter(str(n))
