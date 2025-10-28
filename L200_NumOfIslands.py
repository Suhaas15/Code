class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        islands=0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='0':
                    continue

                islands+=1
                grid[i][j]='0'
                q=deque()
                q.append((i,j))

                while q:
                    orig_i,orig_j=q.popleft()

                    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                        new_i=orig_i+x
                        new_j=orig_j+y

                        if 0<=new_i<rows and 0<=new_j<cols and grid[new_i][new_j]=='1':
                            grid[new_i][new_j]='0'
                            q.append((new_i,new_j))
        
        return islands
        
