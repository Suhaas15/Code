n,m=map(int,input().split())
nums=list(map(int,input().split()))
place=[]
for i in range(m):
    place.append(list(map(int,input().split())))

pos = [0]*(n+1)
for j,num in enumerate(nums):
    pos[num]=j

for i in range(m):
    a,b=place[i]
    a-=1
    b-=1
    nums[a],nums[b] = nums[b],nums[a]
    
    pos[nums[a]]=a
    pos[nums[b]]=b
    rounds=1

    for j in range(2,n+1):
        if pos[j]<pos[j-1]:
            rounds+=1

    print(rounds)
