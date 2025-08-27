class Solution:
    def getMin(self, n: int):
       # code here 
        coins = [1, 2, 5, 10]
        count = 0

        for i in range(len(coins) - 1, -1, -1):  # Start from largest coin
            while n >= coins[i]:
                n -= coins[i]
                count += 1

        return count
