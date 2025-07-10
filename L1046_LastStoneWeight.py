import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max_heap=[-stone for stone in stones]
        max_heap=[]
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            x=-heapq.heappop(max_heap)
            y=-heapq.heappop(max_heap)

            if x!=y:
                heapq.heappush(max_heap,-(x-y))
        
        return -heapq.heappop(max_heap) if max_heap else 0