n=int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: x[1])

count=0
last_end_time=-1

for start,end in times:
    if start>=last_end_time:
        count+=1
        last_end_time=end
print(count)
