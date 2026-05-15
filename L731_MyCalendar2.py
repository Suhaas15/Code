from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.changes = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        self.changes[startTime] += 1
        self.changes[endTime] -= 1

        activeBookings = 0

        for time in sorted(self.changes):
            activeBookings += self.changes[time]

            if activeBookings >= 3:
                self.changes[startTime] -= 1
                self.changes[endTime] += 1

                if self.changes[startTime]==0:
                    del self.changes[startTime]
                if self.changes[endTime]==0:
                    del self.changes[endTime]
                
                return False
            
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
