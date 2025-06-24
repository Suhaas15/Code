class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen={}                       #hash map

        # for i,num in enumerate(numbers):
        #     complement=target-num
        #     if complement in seen and seen[complement]!=i:
        #         return (seen[complement]+1,i+1)
        #     seen[num]=i

        left=0
        right=len(numbers)-1
        while left<right:
            total=numbers[left]+numbers[right]

            if total==target:
                return[left+1,right+1]
            elif total<target:
                left+=1
            else:
                right-=1
        return

