class Solution:
    def maxDifference(self, s: str) -> int:
        count={}
        for char in s:
            count[char] = count.get(char,0) + 1
        #count = Counter(s)
        oddMax, evenMin = 0, len(s)

        for cnt in count.values():
            if cnt%2==0:
                evenMin = min(evenMin, cnt)
            else:
                oddMax = max(oddMax, cnt)
            
        return oddMax-evenMin
