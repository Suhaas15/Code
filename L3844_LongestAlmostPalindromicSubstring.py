class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0

        def helper(l,r):
            while l>=0 and r<n:
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            return r-l-1
        
        for i in range(n):
            for l,r in [[i,i],[i,i+1]]:
                mismatch = False
                while l>=0 and r<n:
                    if s[l]==s[r]:
                        l-=1
                        r+=1
                    else:
                        mismatch = True
                        if l-1>=0 and s[l-1]==s[r]:
                            ans = max(ans, helper(l-1,r))
                        if r+1<n and s[l]==s[r+1]:
                            ans = max(ans, helper(l,r+1))
                        break
                
                if mismatch == False and l >=0 or r<n:
                    ans = max(ans, r-l)
        return ans
