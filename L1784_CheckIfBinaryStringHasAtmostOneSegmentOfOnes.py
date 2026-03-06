class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # return "01" not in s

        seen_zero=False

        for char in s:
            if char=="0":
                seen_zero=True
            if seen_zero==True and char=="1":
                return False
        
        return True

