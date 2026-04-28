import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack=[]
    ans=[]
    maxStack=[]
    
    for string in operations:
        parts=string.split()
        types = int(parts[0])
        
        if types==1:
            val=int(parts[1])
            stack.append(val)
            
            if not maxStack or val>=maxStack[-1]:
                maxStack.append(val)
                
        elif types==2:
            if stack[-1]==maxStack[-1]:
                maxStack.pop()
            stack.pop()
        elif types==3:
            ans.append(maxStack[-1])
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
