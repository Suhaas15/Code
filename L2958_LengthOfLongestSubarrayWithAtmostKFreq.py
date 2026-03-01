from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        n=len(nums)
        l=0
        max_len=0

        for r in range(n):
            freq[nums[r]]+=1

            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1

            max_len=max(max_len,r-l+1)
        
        return max_len
