n=int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

events=[]

for a,b in times:
    events.append((a,1))
    events.append((b,-1))

events.sort(key=lambda x: (x[0], x[1]))

current_customers = 0
max_customers = 0

for event in events:
        current_customers += event[1]
        max_customers = max(max_customers, current_customers)
print(max_customers)
