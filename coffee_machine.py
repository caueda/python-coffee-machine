class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def ask_for_order(self):
        return input("What would you like? (espresso/latte/cappuccino): ").lower()

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}ml")

    def is_there_enough_resources_available(self, coffee):
        ingredients_list = coffee["ingredients"]
        for ingredient in ingredients_list:
            quantity_necessary = ingredients_list[ingredient]
            quantity_available = self.resources[ingredient]
            if quantity_available < quantity_necessary:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True

    def make_coffee_and_deduct_ingredients_from_coffee_machine(self, coffee):
        ingredients_list = coffee["ingredients"]
        for ingredient in ingredients_list:
            quantity_necessary = ingredients_list[ingredient]
            self.resources[ingredient] -= quantity_necessary
