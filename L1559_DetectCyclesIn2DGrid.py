class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i,j,pi,pj,char):
            if visited[i][j]:
                return True
            
            visited[i][j]=True

            for dx,dy in directions:
                ni,nj = i+dx, j+dy

                if 0<=ni<m and 0<=nj<n:
                    if grid[ni][nj]==char:
                        if ni==pi and nj==pj:
                            continue
                        if dfs(ni,nj,i,j,char):
                            return True
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        return False
