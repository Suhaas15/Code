class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count=0
        # for i in nums:
        #     if i!=0:
        #         nums[count]=i
        #         count+=1
        # for i in range(count,len(nums)):
        #     nums[i]=0
        # return nums

        left=right=0                    #2 pointers
        while right!=len(nums):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1
        return nums
