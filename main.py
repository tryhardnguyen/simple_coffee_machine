# COFFEE MACHINE
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

coins = {
    "quarters": .25,
    "dimes": .10,
    "nickles": .05,
    "pennies": .01
}


def calculate(quarters, dimes, nickles, penny):
    money = (coins["quarters"] * quarters) + (coins["dimes"] * dimes) + (coins["nickles"] * nickles) + \
            (coins["pennies"] * penny)
    return round(money, 2)


def resourcesToMakeCoffee(drink):
    # The Question is: How do we subtract only the resources that is needed to make the coffee...
    water_needed = False
    coffee_needed = False
    milk_needed = False
    if "water" in MENU[drink]["ingredients"]:
        water_needed = True
    if "coffee" in MENU[drink]["ingredients"]:
        coffee_needed = True
    if "milk" in MENU[drink]["ingredients"]:
        milk_needed = True
    # If these resources are needed. Subtract it since it used to make the drink
    if water_needed:
        resources["water"] = int(resources["water"] - MENU[drink]["ingredients"]["water"])
    if coffee_needed:
        resources["coffee"] = int(resources["coffee"] - MENU[drink]["ingredients"]["coffee"])
    if milk_needed:
        resources["milk"] = int(resources["milk"] - MENU[drink]["ingredients"]["milk"])
    # Once the values in resources are updated. Return it
    return resources


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


machine_on = True
# While the machine is on
money = 0
while machine_on:
    # TODO: Ask the user What would you like?
    coffee = input("What would you like? (espresso/latte/cappuccino): \n")
    # TODO: If the user type 'report', it show the resources inside the machine like milk,water,coffee
    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    # TODO: If the user type 'off', it turn off the machine
    elif coffee == "off":
        machine_on = False
    # TODO: Bonus feature, worker can refill resources by typing 'water', 'milk', 'coffee'
    elif coffee == "water":
        resources["water"] = 300
    elif coffee == "milk":
        resources["milk"] = 200
    elif coffee == "coffee":
        resources["coffee"] = 100
    else:
        if is_resource_sufficient(MENU[coffee]["ingredients"]):
            # TODO: Print: 'Please insert coins'
            print("Please insert coins")

            # TODO: 'How many quarters?'
            numQuarters = int(input("How many quarters? \n"))

            # TODO: 'How many dimes?'
            numDimes = int(input("How many dimes \n"))
            # TODO: 'How many nickles'
            numNickles = int(input("How many nickles \n"))

            # TODO: 'How many pennies?'
            numPennies = int(input("How many pennies? \n"))

            # TODO: Calculate the totalAmount that the user give
            userAmount = calculate(quarters=numQuarters, dimes=numDimes, nickles=numNickles, penny=numPennies)

            #  TODO: Put the cost of a coffee in a variable
            coffeeCost = MENU[coffee]["cost"]
            # TODO: if the coffeeCost > userAmount
            if coffeeCost > userAmount:
                # TODO: Print: Sorry that's not enough money. Money refunded
                print("Sorry that's not enough money. Money refunded")
            # TODO: if the userAmount > coffeeCost
            elif userAmount > coffeeCost or userAmount == coffeeCost:
                # TODO: Calculate the Change.
                change = userAmount - coffeeCost
                # TODO: Print the change
                print(f"Here's your change: ${change}")
                # TODO: Print "Here's the your {coffee}(coffee emoji)"
                print(f"Here's your {coffee} ☕")
                # TODO: Subtract the resource
                resources = resourcesToMakeCoffee(coffee)
                # TODO: Add the coffeeCost to our money
                money += coffeeCost
