#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        visited=[False]*V
        
        def dfs(node):
            visited[node]=True
            for neighbor in range(V):
                if adj[node][neighbor]==1 and not visited[neighbor]:
                    dfs(neighbor)
                
        
        count=0
        for i in range(V):
            if not visited[i]:
                dfs(i)
                count+=1
            
        return count
