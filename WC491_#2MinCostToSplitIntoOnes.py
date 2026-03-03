class Solution:
    def minCost(self, n: int) -> int:
        #math - most optimal soln
        # return n*(n-1)//2

        #dp soln
        dp = [0]*(n+1)

        for x in range(2,n+1):
            dp[x]=float('inf')

            for a in range(1,x):
                dp[x] = min(dp[x],dp[a] + dp[x-1] + (a*(x-a)))
        
        return dp[n]
