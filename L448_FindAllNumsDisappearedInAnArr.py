class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=set(range(1,n+1))

        for num in nums:
            res.discard(num)
        
        return list(res)
