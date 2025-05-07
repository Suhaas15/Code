class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        reversed_string=str(x)[::-1]
        if string==reversed_string:
            return True
        else:
            return False