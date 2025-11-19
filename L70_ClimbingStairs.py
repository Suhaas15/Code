class Solution:
    def climbStairs(self, n: int) -> int:
        # #Recursion
        # if n==0 or n==1:
        #     return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        # #Memoization
        # def helper(n: int, memo: dict[int,int]) -> int:
        #     if n==0 or n==1:
        #         return 1
        #     if n not in memo:
        #         memo[n] = helper(n-1,memo) + helper(n-2,memo)
        #     return memo[n]

        # memo={}
        # return helper(n,memo)

        #Tabulation
        # if n == 0 or n == 1:
        #     return 1

        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1
        
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        #Space optimization by only taking 2 variables instead of an entire DP table.
        if n==0 or n==1:
            return 1
        prev,curr = 1,1
        for i in range(2,n+1):
            temp=curr
            curr=prev+curr
            prev=temp
        return curr

        

