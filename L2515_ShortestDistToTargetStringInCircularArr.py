class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        res=float('inf')

        for i, word in enumerate(words):
            if word==target:
                dist=abs(i-startIndex)
                res=min(res, dist, n-dist)
        
        return res if res!=float('inf') else -1
