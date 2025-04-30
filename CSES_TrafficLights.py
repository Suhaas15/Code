import bisect

x,n = map(int,input().split())
position = list(map(int,input().split()))

lights=[0,x]
ans=[]

for i in position:
    index=bisect.bisect_left(lights,i)
    lights.insert(index,i)

    max_dist=0
    for j in range(1,len(lights)):
        max_dist=max(max_dist, lights[j]-lights[j-1])
    
    ans.append(max_dist)

print(" ".join(map(str, ans)))

