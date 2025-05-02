n=int(input())
nums=list(range(1,n+1))

pos=0
ans=[]
while(len(nums)>0):
    pos=(pos+1)%len(nums)
    ans.append(nums.pop(pos))

print(" ".join(map(str, ans)))