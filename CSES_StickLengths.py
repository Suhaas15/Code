n=int(input())
lengths=list(map(int,input().split()))

lengths.sort()

if n%2==0:
    median=lengths[n//2-1]
else:
    median=lengths[n//2]

cost=0
for i in lengths:
    cost+=abs(median-i)

print(cost)

