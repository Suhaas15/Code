class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        n = len(ratings)
        left = [1] * n  # Initialize the left array with 1 for each element
        right = [1] * n  # Initialize the right array with 1 for each element
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        
        right=0
        count=0
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right+=1
            else:
                right=0
            count+=max(left[i],right+1)
        
        count+=left[n-1]
        
        return count
        
