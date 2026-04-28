import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    h1_sum, h2_sum, h3_sum = sum(h1), sum(h2), sum(h3)
    
    i=j=k=0
    
    while True:
        #if any sum is 0, we return 0
        if i==len(h1) or j==len(h2) or k==len(h3):
            return 0
        
        #if all sums are equal, return sum
        if h1_sum==h2_sum==h3_sum:
            return h1_sum
        
        if h1_sum>=h2_sum and h1_sum>=h3_sum:
            h1_sum-=h1[i]
            i+=1
        elif h2_sum>=h1_sum and h2_sum>=h3_sum:
            h2_sum-=h2[j]
            j+=1
        else:
            h3_sum-=h3[k]
            k+=1
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
