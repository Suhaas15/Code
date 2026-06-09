class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # count=0
        # for deets in details:
        #     age = int(deets[11:13])
        #     if age>60:
        #         count+=1
            
        # return count

        return sum(int(x[11:13]) > 60 for x in details)
