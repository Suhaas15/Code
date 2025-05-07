class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if not needle:                #Approach with find method
        #     return 0
        # return haystack.find(needle)

        if not needle:
            return 0
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1
        