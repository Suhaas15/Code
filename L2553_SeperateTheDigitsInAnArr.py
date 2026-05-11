class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer=[]

        for num in nums:
            s = str(num)

            for ch in s:
                answer.append(int(ch))
        
        return answer
