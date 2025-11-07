class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dictn = defaultdict(set)
        reslist=[]
        status=[0]*numCourses

        for a,b in prerequisites:
            dictn[a].add(b)
        
        def dfs(node):
            if status[node]==1:
                return False
            if status[node]==2:
                return True
        
            status[node]=1

            for neigh in dictn[node]:
                if not dfs(neigh):
                    return False
                
            status[node]=2
            reslist.append(node)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        
        return reslist
