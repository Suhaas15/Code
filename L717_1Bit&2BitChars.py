class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # n=len(bits)
        # i=0
        # while i<n-1:
        #     i+=bits[i]+1
        # return i==n-1

        bits.pop()
        n = len(bits)

        if n == 0 or bits[-1] == 0:
            return True

        ones = 0
        for i in range(n - 1, -1, -1):
            if bits[i] == 1:
                ones += 1
            else:
                break

        return not (ones & 1)
