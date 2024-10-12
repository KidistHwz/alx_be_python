# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds are available."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
