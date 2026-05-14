class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        return set(nums)==set(range(1,n)) and nums.count(n-1)==2
