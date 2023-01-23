# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class BankAccount:
    bankName = "Bank of America"

    def __init__(self, customer_name, balance, minimum_balance):
        self.customer_name = customer_name
        self.balance = balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        num = self.balance - amount
        if num < self.minimum_balance:
            print("Error, not enough balance")
        else:
            self.balance = self.balance - amount

    def print_Customer_Information(self):
        print(self.customer_name, " has ", self.balance, " dollars in their account at", self.bankName)
        john = BankAccount("john", 3000, 500)
        john.deposit(500)
        john.withdraw(3500)
        steve = BankAccount("steve", 4000, 1000)
        steve.deposit(1000)
        steve.withdraw(500)
        john.print_Customer_Information()
        steve.print_Customer_Information()

