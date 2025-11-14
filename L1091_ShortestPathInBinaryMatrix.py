class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)

        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1

        #BFS queue: (row,col,dist)
        q=deque([(0,0,1)])

        vis=[[False]*n for _ in range(n)]
        vis[0][0]=True
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        while q:
            row,col,dist = q.popleft()

            if row==n-1 and col==n-1:
                return dist
            
            for dr,dc in directions:
                newRow, newCol = row+dr, col+dc

                if 0<=newRow<n and 0<=newCol<n and grid[newRow][newCol]==0 and not vis[newRow][newCol]:
                    vis[newRow][newCol]=True
                    q.append((newRow,newCol,dist+1))
            
        return -1

        
