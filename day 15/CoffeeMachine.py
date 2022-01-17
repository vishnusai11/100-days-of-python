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

machine = 'on'
def check_resource(menu,resource,user_coffee):
    water_required=0
    milk_required=0
    coffee_required=0
    if user_coffee=='espresso':
        water_required = menu[user_coffee]['ingredients']['water']
        coffee_required = menu[user_coffee]['ingredients']['coffee']
        water_present = resource['water']
        coffee_present = resource['coffee']
        water = 'water'
        coffee = 'coffee'
        if water_present > water_required and coffee_present > coffee_required:
            return True
        elif water_present < water_required:
            return water
        elif coffee_present < coffee_required:
            return coffee
    elif user_coffee=='latte' or user_coffee=='cappuccino':
        water_required = menu[user_coffee]['ingredients']['water']
        milk_required = menu[user_coffee]['ingredients']['milk']
        coffee_required = menu[user_coffee]['ingredients']['coffee']
        water_present = resource['water']
        milk_present = resource['milk']
        coffee_present = resource['coffee']
        water = 'water'
        milk = 'milk'
        coffee = 'coffee'
        if water_present>water_required and milk_present>milk_required and coffee_present>coffee_required:
            return True
        elif water_present<water_required:
            return water
        elif milk_present<milk_required:
            return milk
        elif coffee_present<coffee_required:
            return coffee

def calculate(quarters,dimes,nickels,pennies):
    quarters_value=quarters * 0.25
    dimes_value = dimes * 0.10
    nickels_value = nickels * 0.05
    pennies_value = pennies * 0.01
    user_pay=quarters_value+dimes_value+nickels_value+pennies_value
    return user_pay

#machine is running
while machine == 'on':
    user_choice=input('What would you like? (espresso/latte/cappuccino):')
    if user_choice=='espresso' or user_choice=='latte' or user_choice=='cappuccino':
        first_check=check_resource(MENU,resources,user_choice)
        if first_check==True:
            price_of_coffee=MENU[user_choice]['cost']
            print('Please insert coins.\n')
            quarters = int(input('how many quarters?: \n'))
            dimes = int(input('how many dimes?: \n'))
            nickels = int(input('how many nickels?: \n'))
            pennies = int(input('how many pennies?: \n'))
            user_pay=calculate(quarters,dimes,nickels,pennies)
            if user_pay>=price_of_coffee:
                change=user_pay-price_of_coffee
                rounded_change=round(change,2)
                print(f"Here is ${rounded_change} dollars in change.")
                if user_choice=='espresso':
                    resources['money'] = user_pay - rounded_change
                    resources['water'] -= MENU[user_choice]['ingredients']['water']
                    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                    print(f"Here is your {user_choice}. Enjoy!")
                elif user_choice=='latte' or user_choice=='cappuccino':
                    resources['money'] = user_pay-rounded_change
                    resources['water'] -= MENU[user_choice]['ingredients']['water']
                    resources['milk'] -= MENU[user_choice]['ingredients']['milk']
                    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
                    print(f"Here is your {user_choice}. Enjoy!")
            elif user_pay<price_of_coffee:
                print("Sorry that's not enough money. Money refunded.")
                continue
        elif first_check!=True:
            print(f"Sorry there is not enough {first_check}.")
    elif user_choice=='report':
        water=resources['water']
        milk=resources['milk']
        coffee=resources['coffee']
        money=resources['money']
        print(f"Water: {water}ml\n")
        print(f"Milk: {milk}ml\n")
        print(f"Coffee: {coffee}g\n")
        print(f"Money: ${money}\n")
    elif user_choice=='off':
        break