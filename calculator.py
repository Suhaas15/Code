from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1//n2

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

choice="y"

n1=int(input("Enter the first number: "))

while choice=="y" or choice=="n":
    for symbol in operations:
        print(symbol)
    op = input("Pick an operation: ")
    n2 = int(input("What's the next number?: "))
    if op=="+" or op=="-" or op=="*" or op=="/":
        ans = operations[op](n1,n2)
        print(f"{n1} {op} {n2} = {ans}")
    else:
        print("Enter a valid operator!")

    choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
    if choice=="y":
        n1=ans
    elif choice=="n":
        print("\n"*100)
        print(logo)
        n1=int(input("Enter the first number: "))
    else:
        print("Wrong input!")
        break

