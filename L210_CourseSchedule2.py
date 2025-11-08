class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dictn = defaultdict(set)
        # reslist=[]
        # status=[0]*numCourses

        # for a,b in prerequisites:
        #     dictn[a].add(b)
        
        # def dfs(node):
        #     if status[node]==1:
        #         return False
        #     if status[node]==2:
        #         return True
        
        #     status[node]=1

        #     for neigh in dictn[node]:
        #         if not dfs(neigh):
        #             return False
                
        #     status[node]=2
        #     reslist.append(node)
        #     return True
        
        # for node in range(numCourses):
        #     if not dfs(node):
        #         return []
        
        # return reslist
       
        #topo sort problem
        def dfs(node):
            if visited[node] == 1:     # found a cycle
                self.hasCycle = True
                return
            if visited[node] == 2:     # already processed
                return

            visited[node] = 1          # mark as visiting
            for neighbor in adj[node]:
                dfs(neighbor)
                if self.hasCycle:      # stop if a cycle is found
                    return
            visited[node] = 2          # mark as done
            stack.append(node)

        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)           # edge from v → u

        visited = [0] * numCourses     # 0 = unvisited, 1 = visiting, 2 = done
        stack = []
        self.hasCycle = False

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
                if self.hasCycle:      # cycle detected — stop early
                    return []

        return stack[::-1] if not self.hasCycle else []
