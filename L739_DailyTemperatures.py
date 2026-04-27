class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers=[0]*len(temperatures)
        stack=[]

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                index=stack.pop()
                answers[index]=i-index
            stack.append(i)
        
        return answers
