class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        freq=defaultdict(int)

        for i in range(n):
            for j in range(n):
                freq[grid[i][j]]+=1
        
        double=missing=0

        for num in range(1, n**2+1):
            if freq[num]==2:
                double=num
            if freq[num]==0:
                missing=num
        
        return [double,missing]
