class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        score1=0
        score2=0
        active1=True
        active2=False
        game=5

        for i in range(len(nums)):
            if nums[i]%2!=0:
                active1=not active1
                active2=not active2
            if i==game:
                active1,active2 = active2, active1
                game+=6
            
            if active1:
                score1+=nums[i]
            else:
                score2+=nums[i]
        
        return score1-score2

            
