### Data ###
import coins as coins
import self as self

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.money_received = None
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in ingredients:
            if ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coins}? ")) * self.COIN_VALUES[coin]
        return self.money_received

    print("Please insert coins.")

    def transaction_result(self, coins, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
            # if payment is not enough, return False
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False



    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]

    print("Here's your order. Enjoy!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

    def __int__(self):
        self.resources = {
            "bread": 12,
            "ham": 18,
            "cheese": 24,
        }

    def report(self):
        # prints out the report of the resources:
        print(f"bread: {self.resources['bread']}slices")
        print(f"ham: {self.resources['milk']}slices")
        print(f"cheese: {self.resources['coffee']}ounces")

    def make_sandwich(self, order):
        # Deducts the required ingredients from the resources
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here's your {order.name}. Enjoy!")


