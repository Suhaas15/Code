class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total=0
        neg_count=0
        min_abs_val=float('inf')

        for row in matrix:
            for val in row:
                total+=abs(val)
                if val<0:
                    neg_count+=1
                min_abs_val=min(min_abs_val,abs(val))
        
        if neg_count%2==1:
            total-=2*min_abs_val
        
        return total
