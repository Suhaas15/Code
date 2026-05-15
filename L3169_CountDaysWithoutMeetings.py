class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
            
        meetings.sort()

        #merge intervals
        output=[meetings[0]]
        for interval in meetings[1:]:
            lastEnd=output[-1][1]
            if interval[0]<=lastEnd:
                output[-1][1] = max(lastEnd, interval[1])
                continue
            output.append(interval)
        
        #count total meeting days
        count=0
        for interval in output:
            start,end = interval
            count+=end-start+1
        
        return days-count
        
        #can optimize space further but having 2 variables start and end instead of output.
