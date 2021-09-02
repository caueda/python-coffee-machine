from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine
from menu import MENU

coffee_machine = CoffeeMachine()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    order = coffee_machine.ask_for_order()
    if order == "off":
        print("Shutting down the machine")
        machine_is_on = False
    elif order == "report":
        money_machine.report()
        coffee_machine.report()
    else:
        recipe = MENU[order]
        if coffee_machine.is_there_enough_resources_available(recipe):
            given_coins = money_machine.inform_coins()
            if money_machine.process_payment(recipe, given_coins):
                coffee_machine.make_coffee_and_deduct_ingredients_from_coffee_machine(recipe)
                print(f"Here is your {order}. Enjoy!")
        else:
            print("There isn't enough resource")
