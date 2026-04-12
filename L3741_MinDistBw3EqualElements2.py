from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos=defaultdict(list)

        for i, num in enumerate(nums):
            pos[num].append(i)
        
        min_dist = float('inf')

        for indices in pos.values():
            if len(indices)>=3:
                for i in range(len(indices)-2):
                    a,b,c = indices[i], indices[i+1], indices[i+2]
                    dist = abs(a-b)+abs(b-c)+abs(c-a)
                    min_dist = min(dist, min_dist)
        
        return min_dist if min_dist!=float('inf') else -1
