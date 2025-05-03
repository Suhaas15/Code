n,k=map(int,input().split())
nums=list(range(1,n+1))

pos=0
ans=[]
while(len(nums)>0):
    pos=(pos+k)%len(nums)
    ans.append(nums.pop(pos))

print(" ".join(map(str, ans)))
