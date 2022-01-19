from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

machine='on'

while machine=='on':
    choice=menu.get_items()
    user_choice=input(f"What would you like? ({choice}): ")
    if user_choice=='off':
        break
    elif user_choice=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        coffee=menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)