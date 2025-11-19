from typing import List
from collections import deque
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        #Dijkstra's
        if start==end:
            return 0
        
        dist=[float('inf') for i in range(100000)]
        q=deque()
        q.append([0,start])
        
        while q:
            steps,num = q.popleft()
            
            for element in arr:
                new=(num*element)%100000
                
                if steps+1<dist[new]:
                    dist[new]=steps+1
                    if new==end:
                        return steps+1
                    q.append([steps+1,new])
        
        return -1
