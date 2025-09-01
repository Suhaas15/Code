class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # pos=neg=0                     O(n) solution
        # for i in range(len(nums)):
        #     if nums[i]<0:
        #         neg+=1
        #     elif nums[i]>0:
        #         pos+=1
        
        # return max(pos,neg)

        def binary_search(nums,target):
            left,right=0,len(nums)-1
            result=len(nums)

            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]<target:
                    left=mid+1
                else:
                    result=mid
                    right=mid-1
            return result
        
        neg=binary_search(nums,0)
        pos=len(nums)-binary_search(nums,1)
        return max(neg,pos)
        

        
