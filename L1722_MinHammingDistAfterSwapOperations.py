from collections import defaultdict, Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n=len(source)

        graph=defaultdict(list)
        for u,v in allowedSwaps:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=[False]*n
        count=0

        def dfs(node,component):
            stack=[node]

            while stack:
                cur=stack.pop()
                if visited[cur]:
                    continue
                visited[cur]=True
                component.append(cur)
                for neighbor in graph[cur]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        for i in range(n):
            if not visited[i]:
                component=[]
                dfs(i,component)

                src_count = Counter(source[j] for j in component)
                tgt_count = Counter(target[j] for j in component)

                for val in src_count:
                    if val in tgt_count:
                        matched=min(src_count[val], tgt_count[val])
                        src_count[val] -= matched
                
                count+=sum(src_count.values())
        
        return count
