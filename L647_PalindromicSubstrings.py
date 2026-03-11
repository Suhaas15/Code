class Solution:
    def countSubstrings(self, s: str) -> int:
        # n=len(s)            #DP
        # count=0

        # dp=[[False]*n for _ in range(n)]

        # for i in range(n-1,-1,-1):
        #     for j in range(i,n):
        #         if s[i]==s[j] and (j-i+1<=2 or dp[i+1][j-1]):
        #             dp[i][j]=True
        #             count+=1
        
        # return count

        n=len(s)
        count=0

        for i in range(n):
            #odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1

            #even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        
        return count
