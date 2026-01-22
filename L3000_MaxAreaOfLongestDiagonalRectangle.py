class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d=float('-inf')
        max_area=0
        for rect in dimensions:
            d=math.sqrt((rect[0]**2)+(rect[1]**2))
            if d>max_d:
                max_d=d
                max_area=rect[0]*rect[1]
            elif d==max_d:
                max_area=max(max_area, rect[0]*rect[1])
        
        return max_area
