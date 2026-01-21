class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        a=sorted(zip(costs,capacity))
        n=len(a)
        p=[0]*n
        mx=0

        for i in range(n):
            mx=max(mx,a[i][1])
            p[i]=mx
        
        ans=0
        j=n-1
        for i in range(n):
            c,v = a[i]
            if c>=budget:
                break
            ans=max(ans,v)
            while j>=0 and a[j][0]+c>=budget:
                j-=1
            k=min(i-1,j)
            if k>=0:
                ans=max(ans,v+p[k])
        return ans
