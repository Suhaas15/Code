class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt, alt = 0,0

        for i in gain:
            alt+=i
            maxAlt = max(maxAlt, alt)
        
        return maxAlt
