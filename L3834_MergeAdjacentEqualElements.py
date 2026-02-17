class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            curr=i
            while (a and a[-1]==curr):
                curr=a.pop()*2
            a.append(curr)
        return a
