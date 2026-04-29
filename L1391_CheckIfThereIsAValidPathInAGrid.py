class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        i,j = 0,0

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = [[False]*n for _ in range(m)]

        def dfs(i,j):
            if i==m-1 and j==n-1:
                return True
            
            visited[i][j]=True
        
            for dx, dy in directions[grid[i][j]]:
                ni, nj = i+dx, j+dy

                if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                    if (-dx, -dy) in directions[grid[ni][nj]]:
                        if dfs(ni,nj):
                            return True
            return False
        
        return dfs(0,0)
