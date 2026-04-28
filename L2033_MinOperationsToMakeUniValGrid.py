class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #initialize an arr and store all values in it
        nums=[]
        for row in grid:
            for val in row:
                nums.append(val)
        
        #check if remainder of each value with x is the same. Otherwise return -1
        rem=nums[0]%x
        for val in nums:
            if val%x!=rem:
                return -1
        
        #sort the values in the arr and find median
        nums.sort()
        median = nums[len(nums)//2]

        #check no. of operations required
        res=0
        for val in nums:
            res+=abs(val-median)//x
        
        return res
