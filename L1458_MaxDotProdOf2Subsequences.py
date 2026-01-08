class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        #DP
        # m,n = len(nums1), len(nums2)
        # dp = [[float('-inf')]*(n+1) for _ in range(m+1)]

        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         curr_product = nums1[i-1]*nums2[j-1]

        #         dp[i][j] = max(dp[i][j], curr_product, dp[i-1][j], dp[i][j-1], curr_product + dp[i-1][j-1])
        
        # return dp[m][n]

        #optimized
        m,n = len(nums1),len(nums2)

        curr=[float('-inf')]*(n+1)
        prev=[float('-inf')]*(n+1)

        for i in range(1,m+1):
            for j in range(1,n+1):
                curr_prod = nums1[i-1]*nums2[j-1]

                curr[j] = max(curr_prod, prev[j], curr[j-1], curr_prod+max(0,prev[j-1]))
            
            curr,prev=prev,curr
        
        return prev[n]
