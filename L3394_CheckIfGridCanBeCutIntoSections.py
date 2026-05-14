class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(intervals):
            intervals.sort()

            maxEnd = intervals[0][1]
            sections=0

            for start,end in intervals[1:]:
                if maxEnd<=start:
                    sections+=1
                maxEnd=max(maxEnd,end)
            
            return sections>=2

        x_intervals = [[rect[0],rect[2]] for rect in rectangles]
        y_intervals = [[rect[1],rect[3]] for rect in rectangles]

        return check(x_intervals) or check(y_intervals)
