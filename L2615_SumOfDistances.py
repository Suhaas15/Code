class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        seen=defaultdict(list)
        for i,num in enumerate(nums):
            seen[num].append(i)

        res=[0]*len(nums)

        for indices in seen.values():
            prefix_sum=0

            for i, idx in enumerate(indices):
                res[idx]+=idx*i-prefix_sum
                prefix_sum+=idx
            
            prefix_sum=0

            n=len(indices)
            for i in range(n-1,-1,-1):
                idx=indices[i]
                res[idx]+=prefix_sum-idx*(n-1-i)
                prefix_sum+=idx
        
        return res




            
