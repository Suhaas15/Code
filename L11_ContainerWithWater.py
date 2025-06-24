class Solution:
    def maxArea(self, height: List[int]) -> int:
        #naive approach is to use nested for loops
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            area = (right-left)* min(height[left],height[right])

            if height[right]<height[left]:
                right-=1
            else:
                left+=1

            max_area = max(area,max_area)
        
        return max_area