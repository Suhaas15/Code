class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        # ans=[]

        # for num in nums:
        #     ans.append(num)
        
        # for i in range(len(nums)-1,-1,-1):
        #     ans.append(nums[i])
        
        # return ans

        for i in range(len(nums)-1,-1,-1):
            nums.append(nums[i])
        
        return nums

