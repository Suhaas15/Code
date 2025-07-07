class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini=nums[0]
        low=0
        high=len(nums)-1

        while low<high:
            mid=low+(high-low)//2

            if mini>nums[mid]:
                high=mid
            else:
                low=mid+1
        
        if nums[high]<mini:
            return nums[high]
        return mini


            

            
