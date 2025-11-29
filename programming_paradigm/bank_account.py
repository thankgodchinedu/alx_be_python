class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        # Add money to the account
        if amount > 0:
            self.account_balance += float(amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Deduct money if sufficient funds exist
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        amount = float(amount)
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Print the current balance
        print(f"Current Balance: ${self.account_balance:.2f}")

        