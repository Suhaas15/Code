class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Check all possible substrings
        for i in range(n):
            freq = {}
            
            for j in range(i, n):
                # Add current character to frequency map
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                
                # Check if current substring is balanced
                frequencies = list(freq.values())
                if len(set(frequencies)) == 1:  # All frequencies are equal
                    max_len = max(max_len, j - i + 1)
        
        return max_len
