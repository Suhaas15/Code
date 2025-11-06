class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions= [(0,1),(1,0),(-1,0),(0,-1)]
        
        def bfs(x,y):
            queue=deque([(x,y)])
            grid[x][y]=0

            while queue:
                cx,cy = queue.popleft()

                for dx,dy in directions:
                    nx,ny = cx+dx, cy+dy

                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=0
                        queue.append([nx,ny])
        

        for i in range(n):
            if grid[0][i]==1:
                bfs(0,i)
            if grid[m-1][i]==1:
                bfs(m-1,i)
        for i in range(m):
            if grid[i][0]==1:
                bfs(i,0)
            if grid[i][n-1]==1:
                bfs(i,n-1)
        
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
        return count
