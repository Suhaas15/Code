n,m = map(int,input().split())
ticket_prices=list(map(int,input().split()))
max_prices=list(map(int,input().split()))

ticket_prices.sort()

res=[]

for i in max_prices:
    chosen=-1

    for j in range(len(ticket_prices)):
        if ticket_prices[j]<=i:
            chosen=ticket_prices[j]
        else:
            break
    if chosen != -1:
            ticket_prices.remove(chosen)
            res.append(chosen)
    else:
         res.append(-1)
for i in res:
     print(i)
