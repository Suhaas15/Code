class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #if outdegree is 0 add to the queue.
        n=len(graph)
        adj=[[] for _ in range(n)]
        outdegree=[len(graph[i]) for i in range(n)]
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)

        q=deque([i for i in range(n) if outdegree[i]==0])
        safe=[]

        while q:
            curr=q.popleft()
            safe.append(curr)

            for neighbor in adj[curr]:
                outdegree[neighbor]-=1
                if outdegree[neighbor]==0:
                    q.append(neighbor)
        
        return sorted(safe)
