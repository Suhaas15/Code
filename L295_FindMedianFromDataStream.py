import heapq
class MedianFinder:

    def __init__(self):
        self.low=[]
        self.high=[]

    def addNum(self, num: int) -> None:
        if not self.low or num<=-self.low[0]:
            heapq.heappush(self.low,-num)
        else:
            heapq.heappush(self.high,num)
        
        if len(self.low)>len(self.high)+1:
            val=-heapq.heappop(self.low)
            heapq.heappush(self.high,val)
        elif len(self.high)>len(self.low)+1:
            val=heapq.heappop(self.high)
            heapq.heappush(self.low,-val)

    def findMedian(self) -> float:
        if len(self.low)>len(self.high):
            return -self.low[0]
        elif len(self.high)>len(self.low):
            return self.high[0]
        else:
            return (-self.low[0]+self.high[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()