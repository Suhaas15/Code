class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #without stack
        openParanthesesCount=0
        arr=list(s)

        for i in range(len(arr)):
            if arr[i]=="(":
                openParanthesesCount+=1
            elif arr[i]==")":
                if openParanthesesCount==0:
                    arr[i]="*"
                else:
                    openParanthesesCount-=1
        
        for i in range(len(arr)-1,-1,-1):
            if openParanthesesCount>0 and arr[i]=="(":
                arr[i]="*"
                openParanthesesCount-=1
        
        result=''.join(c for c in arr if c!="*")
        return result



        #with stack
        # left=0
        # right=0
        # stack=[]

        # for ch in s:
        #     if ch=='(':
        #         left+=1
        #     elif ch==")":
        #         right+=1
        #     if right>left:
        #         right-=1
        #     else:
        #         stack.append(ch)
        
        # result=""

        # while stack:
        #     curr_char=stack.pop()
        #     if left>right and curr_char=="(":
        #         left-=1
        #     else:
        #         result+=curr_char
        
        # return result[::-1]
