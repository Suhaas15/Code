class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj, node, visited, res):
            visited.add(node)
            res.append(node)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    self.dfsOfGraph(adj,neighbor,visited,res)
                    
    def dfs(self, adj):
        # code here
        # visited=set()             #Iterative
        # stack=[0]
        # res=[]
        
        # while stack:
        #     node=stack.pop()
        #     if node not in visited:
        #         res.append(node)
        #         visited.add(node)
            
        #         for neighbor in reversed(adj[node]):
        #             if neighbor not in visited:
        #                 stack.append(neighbor)
        
        # return res
        
        visited=set()
        res=[]
        self.dfsOfGraph(adj,0,visited,res)
        return res
        
        
