class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        # n=len(nums)                        #O(n) time and O(n) space
        # right_prod=[1]*n

        # for i in range(n-2,-1,-1):
        #     right_prod[i] = right_prod[i+1] * nums[i+1] 

        # left_sum=0
        # for i in range(n):
        #     if left_sum==right_prod[i]:
        #         return i
        #     left_sum+=nums[i]

        # return -1

        # n=len(nums)                        #most space optimal - O(1) space
        # total_prod=1
        # for x in nums:
        #     total_prod*=x

        # left_sum=0
        # left_prod=1

        # for i,x in enumerate(nums):
        #     right_prod = total_prod//(left_prod*x)

        #     if left_sum==right_prod:
        #         return i

        #     left_sum+=x
        #     left_prod*=x

        # return -1

        lsum, rprod = sum(nums), 1
        for i in reversed(range(len(nums))):
            lsum -= nums[i]  # Update from sum(nums[0..i]) -> sum(nums[0..i-1])
            if lsum == rprod:
                return i
            if lsum < rprod:  # rprod can only increase, while lsum only decrease, so there no more matches
                break

            rprod *= nums[i]  # Update from prod(nums[i+1...n-1]) -> prod(nums[i..n-1])

        return -1
