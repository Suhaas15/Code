class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n=len(s)            #DP
        # resIdx=0
        # resLen=0

        # dp=[[False]*n for _ in range(n)]

        # for i in range(n-1,-1,-1):
        #     for j in range(i,n):
        #         if s[i]==s[j] and (j-i+1<=2 or dp[i+1][j-1]):
        #             dp[i][j]=True
        #             if resLen<j-i+1:
        #                 resLen=j-i+1
        #                 resIdx=i
                    
        # return s[resIdx:resLen+resIdx]

        resIdx=0            
        resLen=0
        n=len(s)

        for i in range(n):
            #odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resLen=r-l+1
                    resIdx=l
                
                l-=1
                r+=1
            
            #even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    resLen=r-l+1
                    resIdx=l
                
                l-=1
                r+=1
            
        return s[resIdx : resIdx+resLen]
