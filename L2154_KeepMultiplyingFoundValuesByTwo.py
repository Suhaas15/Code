class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        found=True
        numbers=set(nums)

        while found:
            if original in numbers:
                original=2*original
            else:
                found=False
        
        return original
