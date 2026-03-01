class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraycounter(nums,k,l):
            ans=0
            i=0
            d=dict()

            for j in range(l):
                if nums[j] in d:
                    d[nums[j]]+=1
                else:
                    d[nums[j]]=1
                
                while len(d)>k:
                    d[nums[i]]-=1
                    if d[nums[i]]==0:
                        del d[nums[i]]
                    i+=1
                ans+=j-i+1
            
            return ans
            
        #Exactly k distinct = At most k distinct − At most (k − 1) distinct

        l=len(nums)
        return subarraycounter(nums,k,l) - subarraycounter(nums,k-1,l)
        
        
