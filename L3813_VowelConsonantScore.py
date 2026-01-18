class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i in 'aeiou':
                    v = v+1
                else:
                    c = c+1
        if c > 0:
            return v // c
        else:
            return 0
