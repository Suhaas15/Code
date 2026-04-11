class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        total=0
        diff = []
        for i in range(len(capacity)):
            if rocks[i]==capacity[i]:
                total+=1
            else:
                diff.append(capacity[i] - rocks[i])
        
        diff.sort()

        for i in diff:
            if additionalRocks==0:
                break
            if additionalRocks>=i:
                additionalRocks-=i
                total+=1
            else:
                additionalRocks=0
        
        return total
            

        

