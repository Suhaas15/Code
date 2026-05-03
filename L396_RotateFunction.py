class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ##n-square soln
        # maxVal=0
        # for i in range(len(nums)):
        #     total=0
        #     for i,num in enumerate(nums):
        #         total+=i*num
        #     maxVal = max(maxVal, total)

        #     nums.insert(0, nums.pop())
        
        # return maxVal

        n=len(nums)
        total=sum(nums)

        F = sum(i*num for i,num in enumerate(nums))

        maxVal=F
        for k in range(1,n):
            F = F + total - n * nums[-k]
            maxVal=max(maxVal, F)
        
        return maxVal
