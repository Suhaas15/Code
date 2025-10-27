class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])

        visited=set()
        tcolor=image[sr][sc]

        def paint(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=tcolor or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            image[r][c]=color

            # paint(r+1,c)              can either call recursively like this or use a for loop as below.
            # paint(r-1,c)
            # paint(r,c+1)
            # paint(r,c-1)

            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx,yy=r+x,c+y
                paint(xx,yy)
        
        paint(sr,sc)

        return image
