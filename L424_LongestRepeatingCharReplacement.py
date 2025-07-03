from typing import List
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        ans=0
        max_count=0
        counts=[0]*26

        for right in range(len(s)):
            char=s[right]
            index=ord(char)-ord('A')
            counts[index]+=1
            max_count = max(max_count,counts[index])

            window_size = right-left+1
            if window_size-max_count>k:
                #decrease the window size
                char=s[left]
                index=ord(char)-ord('A')
                counts[index]-=1
                left+=1
            
            ans=max(ans,right-left+1)
        
        return ans
