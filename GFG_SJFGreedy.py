#User function Template for python3

class Solution:
    def solve(self, bt):
        # Code here
        bt.sort()
        sum=0
        t=0
        
        for time in bt:
            sum+=t
            t+=time
        
        avg=sum/len(bt)
        
        return int(avg)
            
            
