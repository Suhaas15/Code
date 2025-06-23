class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        # nums.sort()               #with sorting
        # count=1
        # maxi=1
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         continue
        #     elif nums[i]+1==nums[i+1]:
        #         count+=1
        #         maxi=max(count,maxi)
        #     else:
        #         count=1
        # return maxi

        res=set(nums)
        n=len(nums)
        maxi=0

        for i in res:
            if i-1 not in res:
                length=1
                while i+length in res:
                    length+=1
                maxi=max(length,maxi)
        return maxi

