class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        m,n = len(board), len(board[0])
        queue=deque()

        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        for i in range(m):
            for j in [0,n-1]:
                if board[i][j]=='O':
                    queue.append((i,j))

        for j in range(n):
            for i in [0,m-1]:
                if board[i][j]=='O':
                    queue.append((i,j))

        while queue:
            x,y=queue.popleft()
            if board[x][y]=='O':
                board[x][y]='S'
                for dx,dy in directions:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                        queue.append((nx,ny))
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'
