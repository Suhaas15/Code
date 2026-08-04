class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)

        for char in ransomNote:
            if mag_count[char]:
                mag_count[char]-=1
            else:
                return False
        
        return True
