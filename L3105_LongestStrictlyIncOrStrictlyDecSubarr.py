class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        IncCount, DecCount, maxCount = 1,1,1

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                IncCount+=1
                DecCount=1
            elif nums[i]>nums[i+1]:
                IncCount=1
                DecCount+=1
            else:
                IncCount=1
                DecCount=1
            
            maxCount = max(maxCount, IncCount, DecCount)

        return maxCount
