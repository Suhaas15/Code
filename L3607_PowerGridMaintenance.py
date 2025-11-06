class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        if px!=py:
            self.parent[py]=px

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)

        for a,b in connections:
            dsu.union(a,b)
        
        from collections import defaultdict
        import bisect
        groups=defaultdict(list)
        for i in range(1,c+1):
            root=dsu.find(i)
            groups[root].append(i)
        for g in groups.values():
            g.sort()
        
        isOffline = [False]*(c+1)
        res=[]

        for typ,node in queries:
            if typ==1:
                if not isOffline[node]:
                    res.append(node)
                else:
                    root=dsu.find(node)
                    arr=groups.get(root,[])
                    res.append(arr[0] if arr else -1)
            else:
                if not isOffline[node]:
                    isOffline[node]=True
                    root=dsu.find(node)
                    arr=groups.get(root,[])
                    idx=bisect.bisect_left(arr,node)
                    if idx<len(arr) and arr[idx]==node:
                        arr.pop(idx)
        
        return res
                
