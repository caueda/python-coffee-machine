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
    "money":0.0
}

def printResourcesAvailable():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['money']}")

def isThereEnoughResourcesAvailable(recipe):
    ingredients_list = recipe["ingredients"]
    for ingredient in ingredients_list:
        quantity_necessary = ingredients_list[ingredient]
        quantity_available = resources[ingredient]
        if quantity_available < quantity_necessary:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def deductIngredientsFromCoffeeMachine(recipe):
    ingredients_list = recipe["ingredients"]
    for ingredient in ingredients_list:
        quantity_necessary = ingredients_list[ingredient]
        resources[ingredient] -= quantity_necessary

def processPayment(recipe, givenMoney):
    """Check if payment is accepted return the value of the change. Returns a number less than zero if not accepted, and a number greater or equal to zero if accepted."""
    cost = recipe["cost"]
    return givenMoney - cost

def informTheCoins():
    """Return the total value of money inserted"""
    total = 0.0
    print("Please insert coins.")
    total += (float(input("How many quarters?: ")) * 0.25)
    total += (float(input("How many dimes?: ")) * 0.10)
    total += (float(input("How many nickles?: ")) * 0.05)
    total += (float(input("How many pennies?: ")) * 0.01)
    return total

machine_is_on = True
while machine_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        print("Shutting down the machine")
        machine_is_on = False
    elif order == "report":
        printResourcesAvailable()
    else:
        recipe = MENU[order]
        if isThereEnoughResourcesAvailable(recipe):
            givenMoney = informTheCoins()
            change = processPayment(recipe, givenMoney)
            if change < 0.0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["money"] += givenMoney - change
                if change > 0.0:
                    print(f"Here is ${round(change,2)} dollars in change.")
                deductIngredientsFromCoffeeMachine(recipe)
                print(f"Here is your {order}. Enjoy!")    
        else:
            print("There isn't enough resource")

