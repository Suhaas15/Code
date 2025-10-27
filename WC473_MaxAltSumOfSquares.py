class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[x*x for x in nums]
        nums.sort()
        res=[0]*len(nums)

        j=0
        for i in range(len(nums)):
            if i%2!=0:
                res[i]=nums[j]
                j+=1

        for i in range(len(nums)):
            if i%2==0:
                res[i]=nums[j]
                j+=1

        score=0
        for i in range(len(nums)):
            if i%2==0:
                score+=res[i]
            else:
                score-=res[i]

        return score
        
