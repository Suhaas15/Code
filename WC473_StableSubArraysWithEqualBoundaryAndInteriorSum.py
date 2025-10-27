class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        count = 0
        n = len(capacity)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + capacity[i - 1]
        position_map = {}
        
        for r in range(n):
            if r >= 2:
                l = r - 2
                key = (capacity[l], prefix_sum[l + 1])
                position_map[key] = position_map.get(key, 0) + 1
            
            if r >= 2:
                target_value = capacity[r]
                target_prefix = prefix_sum[r] - capacity[r]
                key = (target_value, target_prefix)
                
                count += position_map.get(key, 0)
        
        return count
            
                
            
