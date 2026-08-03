class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)

        if n%2!=0:
            return False
        
        count=Counter(nums)

        for key,val in count.items():
            if val%2!=0:
                return False
        
        return True
