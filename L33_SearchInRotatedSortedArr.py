class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        if len(nums)==1:
            return 0 if target==nums[0] else -1
        
        low,high=0,len(nums)-1

        while low<=high:
            mid=low+(high)-low//2

            if target==nums[mid]:
                return mid
            elif nums[low]<=nums[mid]:      #left half is sorted
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:                           #right half is sorted
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return -1       