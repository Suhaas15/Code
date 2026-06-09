class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        total=max(nums)-min(nums)

        return total*k
