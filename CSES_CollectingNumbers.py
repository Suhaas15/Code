n=int(input())
nums=list(map(int,input().split()))

# last=max(nums)
# j=1
# count=0
# ans=[]

# while j<=last:
#     for i in range(n):
#         if nums[i]==j:
#             j+=1
#     count+=1

# print(count)

pos = [0]*(n+1)
for i,num in enumerate(nums):
    pos[num]=i

rounds=1

for i in range(2,n+1):
    if pos[i]<pos[i-1]:
        rounds+=1

print(rounds)

