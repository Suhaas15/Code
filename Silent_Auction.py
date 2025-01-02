from art import logo

print(logo)
print("Welcome to Silent Auction!!")

more="yes"
bids={}
max=0
while more=="yes":
    name=input("What is your name?: ")
    amt=int(input("What's your bid?: $"))
    check=input("Are there any other bidders?: ").lower()
    bids[name]=amt
    if check=="yes":
        print("\n"*100)
    if check=="no":
        more="no"
        for i in bids:
            if bids[i]>max:
                max=bids[i]
                name=i
print(f"The winner is {name} with a bid of {max}")


