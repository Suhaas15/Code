class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitSum(n):
            total=0
            while n:
                digit=n%10
                n=n//10
                total+=digit
            return total

        for i in range(len(nums)):
            nums[i]=digitSum(nums[i])
        
        return min(nums)
