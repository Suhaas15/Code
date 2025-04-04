n = int(input("")) 
numbers = [int(x) for x in input().split()]  

res = set()  
for num in numbers:
    res.add(num) 


print(len(res))
