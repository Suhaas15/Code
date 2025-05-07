class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={')':'(', '}':'{', ']':'['}

        for i in s:
            if i in match.values():
                stack.append(i)
            elif i in match:
                if not stack or stack[-1] != match[i]:
                    return False
                stack.pop()
        
        return len(stack)==0