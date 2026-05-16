class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQueries = sorted((q,i) for i,q in enumerate(queries))
        res=[-1]*len(queries)
        heap=[]
        i=0

        for q,idx in sortedQueries:
            while i<len(intervals) and intervals[i][0]<=q:
                l,r = intervals[i]
                size=r-l+1
                heapq.heappush(heap, (size, r))
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            
            if heap:
                res[idx]=heap[0][0]

        return res
