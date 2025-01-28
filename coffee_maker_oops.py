from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    print(menu.get_items())
    choice = input("Your order: ")
    if choice == "off":
        print("Byee!!")
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
       if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
           if money_machine.make_payment(menu.find_drink(choice).cost):
               coffee_maker.make_coffee(menu.find_drink(choice))
    elif choice == "refill":
        coffee_maker.refill()
    else:
        print("Wrong input!! Try again!")

