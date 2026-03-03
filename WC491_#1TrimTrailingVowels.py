class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        r=len(s)-1
        while r>=0:
            if not s[r]=="a" and not s[r]=="e" and not s[r]=="i" and not s[r]=="o" and not s[r]=="u":
                break
            r-=1
        
        return s[:r+1]
