class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0

        for char in s:
            if len(t)==i:
                return 0
            
            if char==t[i]:
                i+=1
        
        return len(t)-i
