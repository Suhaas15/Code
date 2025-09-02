import heapq
class Solution:
    def jobSequencing(self, deadline, profit):
        # n=len(deadline)               #naive - O(n^2)
        # count=0
        # total_profit=0
        
        # jobs=sorted(zip(profit,deadline), reverse=True)
        
        # slot=[0]*n
        # for i in range(n):
        #     start=min(n,jobs[i][1])-1
        #     for j in range(start,-1,-1):
        #         if slot[j]==0:
        #             slot[j]=1
        #             count+=1
        #             total_profit+=jobs[i][0]
        #             break
        
        # return [count,total_profit]
        
        n=len(deadline)                 #sort and priority queue
        ans=[0,0]
        
        jobs = sorted(zip(deadline, profit))
        
        pq=[]
        
        for job in jobs:
            if job[0]>len(pq):
                heapq.heappush(pq,job[1])
            elif pq and pq[0]<job[1]:
                heapq.heappop(pq)
                heapq.heappush(pq,job[1])
        
        while pq:
            ans[1]+=heapq.heappop(pq)
            ans[0]+=1
        
        return ans
        
