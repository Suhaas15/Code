import bisect

n=int(input())
sizes = list(map(int,input().split()))

towers=[]

for cube in sizes:
    # Find first tower where cube can be placed (cube < top)
    pos = bisect.bisect_right(towers, cube)
    
    if pos < len(towers):
        towers[pos] = cube  # Replace the top of that tower
    else:
        towers.append(cube)  # No suitable tower → start new one


# towers.append(sizes[0])

# for i in range(1,n):
#     flag=0
#     for j in range(len(towers)):
#         if sizes[i]<towers[j]:
#             towers[j]=sizes[i]
#             flag=1
#             break
#     if flag==0:
#         towers.append(sizes[i])

print(len(towers))

