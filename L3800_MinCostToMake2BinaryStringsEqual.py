class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        c=[0,0]
        for a,b in zip(s,t):
            if a!=b:
                c[int(a)]+=1
        c0,c1=c
        res1=(c0+c1)*flipCost
        res2=min(c0,c1) * swapCost + abs(c0-c1)*flipCost
        res3=min(c0,c1) * swapCost + abs(c0-c1)//2 * (swapCost+crossCost) + abs(c0-c1)%2 * flipCost
        return min(res1,res2,res3)

        #res1 - Directly flip every mismatch using flipCost
        #res2 - Resolve c0,c1 pairs using swapCost, then flip all remaining same-type mismatches
        #res3 - Resolve pairs using swapCost, for the remaining mismatches of same type, pair them using one crossCost and one swapCost to fix 2 at once. Any final single mismatch is handled with a flip.
        
         
