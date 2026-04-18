class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            return int(str(x)[::-1])
        
        res=float('inf')
        seen={}

        for i, num in enumerate(nums):
            if num in seen:
                res=min(res, i-seen[num])
            
            seen[reverse(num)]=i
        
        return res if res!=float('inf') else -1
