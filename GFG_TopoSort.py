class Solution:
    def topoSort(self, V, edges):
        # Code here
        def dfs(node,visited):
            visited[node]=True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor,visited)
            
            stack.append(node)
        
        visited=[False]*V
        stack=[]
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        for i in range(V):
            if not visited[i]:
                dfs(i,visited)
        
        return stack[::-1]
