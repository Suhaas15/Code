import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # def findDivisors(n):
        #     curr=0
        #     count=0

        #     for i in range(1,n+1):
        #         if n%i==0:
        #             count+=1
        #             curr+=i
        #     if count==4:
        #         return curr
        #     else:
        #         return 0
        
        # total=0
        # for i in nums:
        #     total+=findDivisors(i)
        
        # return total

        total_sum=0

        for i in nums:
            div_count,curr_sum=0,0

            for divisor in range(1, int(math.sqrt(i))+1):
                if i%divisor==0:
                    other=i//divisor
                    if divisor==other:      #square
                        div_count+=1
                        curr_sum+=divisor
                    else:
                        div_count+=2
                        curr_sum+=divisor+other
                    
                    if div_count>4:
                        break
            
            if div_count==4:
                total_sum+=curr_sum
        
        return total_sum
