
from dict_file import menu, resources
cash = 0


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry, there is not enough {}.".format(item))
            return False
    return True


def take_payment():
    print("Please enter coins.")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.10
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total


def check_payment(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print("Here is your change : ${}".format(change))
        global cash
        cash += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your {} 😎. Enjoy!".format(drink_name))


is_on = True
while is_on:
    choice = input("What would you like? (espresso/ latte / cappuccino) : ").lower()
    if choice == 'off' or choice == 'report' or choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            print("Water : {}ml".format(resources['water']))
            print("Milk : {}ml".format(resources['milk']))
            print("Coffee : {}g".format(resources['coffee']))
            print("Cash : ${}".format(cash))
        else:
            drink = menu[choice]
            # TODO 1 : Check if resources are sufficient
            if check_resources(drink['ingredients']):
                # TODO 2 : Collect coins
                payment = take_payment()
                # TODO 3 : Check if payment is sufficient
                if check_payment(payment, drink['cost']):
                    # TODO 4 : Make coffee
                    make_coffee(choice, drink['ingredients'])
    else:
        print("Sorry, please make a valid choice. : ")
