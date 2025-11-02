class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1,d2=d
        r1,r2=r

        def lcm(a,b):
            return a//gcd(a,b)*b

        L=lcm(r1,r2)

        def can(T:int)->bool:
            a1=T-T//r1
            a2=T-T//r2

            cap=T-T//L
            return a1>=d1 and a2>=d2 and cap>=d1+d2

        lo,hi=0,(d1+d2+1)*max(1,r1,r2)
        while lo<hi:
            mid=(lo+hi)//2
            if can(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
