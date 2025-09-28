from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        visited=set()
        queue=deque([0])
        visited.add(0)
        res=[]
        
        while queue:
            node=queue.popleft()
            res.append(node)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return res
