class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq={}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        total=0
        for key,val in freq.items():
            if val%k==0 or val==0:
                total+=key*val

        return total
            
