n,x=map(int,input().split())
nums=list(map(int,input().split()))

def two_sum(n,x,nums):
    num_map={}
    for i in range(n):
        target=x-nums[i]
        if target in num_map:
            print(num_map[target],i+1)
            return
        num_map[nums[i]]=i+1
    print("IMPOSSIBLE")
two_sum(n,x,nums)

# ans=[]
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==x:
#             ans.append(i+1)
#             ans.append(j+1)
# if len(ans)==0:
#     print("IMPOSSIBLE")
# else:
#     print(ans[0],ans[1])
    

