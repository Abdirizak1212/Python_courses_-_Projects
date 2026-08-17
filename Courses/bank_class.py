class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

# Test it
account = BankAccount("Nadaara", 1000)
account.show_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)