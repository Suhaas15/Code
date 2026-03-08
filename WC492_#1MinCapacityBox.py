class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        if len(capacity)<=1:
            return 0 if capacity and capacity[0] >= itemSize else -1
        min_cap=float('inf')
        min_ind=-1
        for i in range(len(capacity)):
            if itemSize<=capacity[i] and min_cap>capacity[i]:
                min_cap=capacity[i]
                min_ind=i

        return min_ind
