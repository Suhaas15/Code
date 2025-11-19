class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for x,y,w in times:
            adj[x].append((w,y))
        
        visited=set()
        heap=[(0,k)]

        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)

            if len(visited)==n:
                return travel_time
            
            for time, adj_node in adj[node]:
                if adj_node not in visited:
                    heapq.heappush(heap,(time+travel_time,adj_node))
        
        return -1
