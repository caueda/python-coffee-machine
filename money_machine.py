class MoneyMachine:
    def __init__(self):
        self.cash = 0.0
        self.coins =[0, 0, 0, 0]

    def inform_coins(self):
        print("Please insert coins.")
        received_coins = [0, 0, 0, 0]
        received_coins[0] = int(input("How many quarters?: "))
        received_coins[1] = int(input("How many dimes?: "))
        received_coins[2] = int(input("How many nickles?: "))
        received_coins[3] = int(input("How many pennies?: "))
        return received_coins

    def calculate_change(self, change_value):
        coins = [0, 0, 0, 0]
        while(change_value > 0):
            if change_value >= 0.25:
                coins[3] += 1
                change_value -= 0.25
            elif change_value >= 0.10:
                coins[2] += 1
                change_value -= 0.10
            elif change_value >= 0.05:
                coins[1] += 1
                change_value -= 0.01
        return coins

    def report(self):
        print(f"Money: ${round(self.cash, 2)}")

    def process_payment(self, coffee, coins):
        """Check if payment is accepted return the value of the change. Returns a number less than zero if not accepted,
        and a number greater or equal to zero if accepted. """
        price = coffee["cost"]
        total = coins[0] * 0.25
        total += coins[1] * 0.10
        total += coins[2] * 0.05
        total += coins[3] * 0.01
        change = total - price
        if change >= 0.0:
            self.coins[0] += coins[0]
            self.coins[1] += coins[1]
            self.coins[2] += coins[2]
            self.coins[3] += coins[3]
            if change > 0:
                coins = self.calculate_change(change)
                print(f"Here's your change {coins[3]} quarters, {coins[2]} dimes, {coins[1]} nickles, {coins[0]} pennies")
            self.cash += price
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False



