class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topo sort problem
        def dfs(node):
            if hasCycle[0]:
                return
            if visited[node]==1:
                hasCycle[0]=True
                return
            if visited[node]==2:
                return
            
            visited[node]=1
            for neighbor in adj[node]:
                dfs(neighbor)
                if hasCycle[0]:
                    return
            visited[node]=2
        
        visited=[0]*numCourses
        hasCycle=[False]
        adj=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)

        for i in range(numCourses):
            if visited[i]==0:
                dfs(i)
                if hasCycle[0]:
                    return False
        
        return True
