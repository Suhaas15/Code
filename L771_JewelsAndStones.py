class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen=set(jewels)
        count=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                count+=1
        return count