from collections import defaultdict
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n=len(arr)
        groups=defaultdict(list)

        for i,num in enumerate(arr):
            groups[num].append(i)

        res=[0]*n

        for group in groups.values():
            total=sum(group)
            prefixSum = 0
            size=len(group)

            for i,idx in enumerate(group):
                res[idx]+= total - prefixSum * 2 + idx * (2*i-size)
                prefixSum+=idx
        
        return res
