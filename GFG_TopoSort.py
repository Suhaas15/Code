from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # def dfs(node,visited):
        #     visited[node]=True
            
        #     for neighbor in adj[node]:
        #         if not visited[neighbor]:
        #             dfs(neighbor,visited)
            
        #     stack.append(node)
        
        # visited=[False]*V
        # stack=[]
        # adj=[[] for _ in range(V)]
        # for u,v in edges:
        #     adj[u].append(v)
        # for i in range(V):
        #     if not visited[i]:
        #         dfs(i,visited)
        
        # return stack[::-1]
        
        #Kahn's Algorithm
        adj = [[] for _ in range(V)]        #build adjacency list
        for u, v in edges:
            adj[u].append(v)
        in_degree=[0 for _ in range(V)]     #build indegree list
        for u in range(V):
            for v in adj[u]:
                in_degree[v] += 1
        
        queue=deque([node for node in range(V) if in_degree[node]==0])      #initialize the queue
        topo_order=[]
        
        while queue:                        #pop from queue and reduce indegree of neighbors by 1
            node=queue.popleft()
            topo_order.append(node)
            
            for neighbor in adj[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        
        if len(topo_order)!=V:      #check for cycles
            return []
        
        return topo_order
            
