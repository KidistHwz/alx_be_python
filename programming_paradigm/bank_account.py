# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance."""
        self.__account_balance = initial_balance  # Encapsulation: private attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if there are sufficient funds."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        print("Insufficient funds.")
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
