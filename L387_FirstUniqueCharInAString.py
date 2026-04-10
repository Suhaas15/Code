class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}

        for char in s:
            freq[char] = 1+freq.get(char,0)

        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
        
        
