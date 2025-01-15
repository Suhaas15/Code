MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")

def check_resources(drink):
    if drink=="latte" or drink=="cappuccino":
        if resources['water']>=MENU[drink]['ingredients']['water']:
            if resources['milk']>=MENU[drink]['ingredients']['milk']:
                if resources['coffee']>=MENU[drink]['ingredients']['coffee']:
                    return True
                else:
                    print("Sorry there is not enough coffee!")
                    return False
            else:
                print("Sorry there is not enough milk!")
                return False
        else:
            print("Sorry there is not enough water!")
            return False
    elif drink=="espresso":
        if resources['water']>=MENU[drink]['ingredients']['water']:
            if resources['coffee']>=MENU[drink]['ingredients']['coffee']:
                return True
            else:
                print("Sorry there is not enough coffee!")
                return False
        else:
            print("Sorry there is not enough water!")
            return False
    else:
        print("Wrong input!")
        return False

def bank():
    global money
    q=float(input("How many quarters?: "))
    d=float(input("How many dimes?: "))
    n=float(input("How many nickels?: "))
    p=float(input("How many pennies?: "))
    total_money = int((q*0.25)+(d*0.1)+(n*0.05)+(p*0.01))
    if total_money>=MENU[choice]['cost']:
        refund=total_money-MENU[choice]['cost']
        money+=(total_money-refund)
        if refund>0:
            print(f"Here is ${refund} dollars in change.")
        return True
    elif total_money<MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded!")
        return False

def use():
    if choice=="latte" or choice=="cappuccino":
        resources["water"]-=MENU[choice]['ingredients']['water']
        resources['milk']-=MENU[choice]['ingredients']['milk']
        resources['coffee']-=MENU[choice]['ingredients']['coffee']
        print(f"Here's your {choice} ☕️. Enjoy!")
    elif choice=="espresso":
        resources["water"] -= MENU[choice]['ingredients']['water']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']

def refill():
    resources["water"]=300
    resources["milk"]=200
    resources["coffee"]=100

money=0

while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="report":
        report()
    elif choice=="off":
        break
    elif choice=="latte" or choice=="cappuccino" or choice=="espresso":
        if check_resources(choice):
            if bank():
                use()
    elif choice=="refill":
        refill()
    else:
        print("Wrong input!! Try again!")