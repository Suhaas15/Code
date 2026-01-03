class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # freq={}

        # for x in nums:
        #     if x in freq:
        #         freq[x]+=1
        #     else:
        #         freq[x]=1
        
        # for key,val in freq.items():
        #     if val>1:
        #         return key

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:                
                return nums[i]
            elif i+2<len(nums) and nums[i]==nums[i+2]:
                return nums[i]
            elif i+3<len(nums) and nums[i]==nums[i+3]:
                return nums[i]
