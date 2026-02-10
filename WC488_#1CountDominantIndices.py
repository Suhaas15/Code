class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        # def avg(index):
        #     total=0
        #     for i in range(index,len(nums)):
        #         total+=nums[i]
        #     avg=total/(len(nums)-index)
        #     return avg
        # count=0
        # for i in range(len(nums)-1):
        #     if nums[i]>avg(i+1):
        #         count+=1
        # return count

        n=len(nums)
        suffix_sum = sum(nums)
        count=0

        for i in range(n-1):
            suffix_sum-=nums[i]
            avg=suffix_sum/(n-i-1)
            if nums[i]>avg:
                count+=1
        
        return count

