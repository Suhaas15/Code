class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0

        for word in words:
            flag=True
            for char in word:
                if char not in allowed:
                    flag=False
            
            if flag:
                res+=1
        
        return res
