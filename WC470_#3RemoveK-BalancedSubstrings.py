class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack=[]

        for char in s:
            if stack and stack[-1][0]==char:
                stack[-1]= (char, stack[-1][1] + 1)
            else:
                stack.append((char,1))

            if len(stack)>=2:
                if stack[-1][0] == ')' and stack[-1][1] >= k:
                    if stack[-2][0] == '(' and stack[-2][1] >= k:
                        open_count = stack[-2][1] - k
                        close_count = stack[-1][1] - k

                        stack.pop()  
                        stack.pop() 

                        if open_count > 0:
                            stack.append(('(', open_count))
                        if close_count > 0:
                            stack.append((')', close_count))

        return ''.join(char * count for char, count in stack)
            
    

        
