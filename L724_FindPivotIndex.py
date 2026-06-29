class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # n=len(nums)
        # leftSum, rightSum = [0]*n, [0]*n

        # total=nums[0]
        # for i in range(1, n):
        #     leftSum[i] = total
        #     total += nums[i]
        
        # total=nums[n-1]
        # for i in range(n-2,-1,-1):
        #     rightSum[i]=total
        #     total+=nums[i]
        
        # for i in range(n):
        #     if leftSum[i]==rightSum[i]:
        #         return i
        
        # return -1

        total=sum(nums)
        leftSum=0

        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum+=nums[i]
        
        return -1
