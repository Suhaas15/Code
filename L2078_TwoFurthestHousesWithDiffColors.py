class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        maxDist=0

        for i in range(n):
            if colors[i]!=colors[0]:
                maxDist=max(maxDist, i)
            if colors[i]!=colors[-1]:
                maxDist=max(maxDist, n-1-i)
        
        return maxDist
