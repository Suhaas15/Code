class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m,n = len(boxGrid), len(boxGrid[0])

        #gravity
        for i in range(m):
            pointer=n-1
            for j in range(n-1,-1,-1):
                if boxGrid[i][j]==".":
                    continue
                if boxGrid[i][j]=="#":
                    boxGrid[i][j]="."
                    boxGrid[i][pointer] = "#"
                    pointer-=1
                if boxGrid[i][j]=="*":
                    pointer=j-1
        
        #rotate
        ans=[["."]*m for i in range(n)]
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[0])):
                ans[j][m-1-i]=boxGrid[i][j]
        
        return ans
