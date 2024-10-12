# bank_account.py

class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance, defaulting to 0."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount to the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds are available."""
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdraw amount must be positive.")
            return False

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current Balance: ${self.account_balance:.2f}")
