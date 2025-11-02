class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        ans=[]
        my_set=set(nums)
        for i in range(nums[0]+1,nums[n-1]+1):
            if i not in my_set:
                ans.append(i)
        return ans
