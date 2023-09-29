class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")


# Example usage
account = BankAccount("12345")
account.deposit(1000)  # Output: Deposited $1000. New balance: $1000
account.withdraw(500)  # Output: Withdrew $500. New balance: $500
account.withdraw(1000)  # Output: Insufficient funds!
