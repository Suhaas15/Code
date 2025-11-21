class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])

        #x,y,obstacles,steps
        q=deque([(0,0,k,0)])
        seen=set()
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            x,y,left,steps=q.popleft()
            if (x,y,left) in seen or left<0:
                continue
            if (x,y)==(m-1,n-1):
                return steps
            seen.add((x,y,left))
            if grid[x][y]==1:
                left-=1
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n:
                    q.append((nx,ny,left,steps+1))
        
        return -1
