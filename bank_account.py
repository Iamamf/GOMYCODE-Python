# Create a class called "Account"
class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient funds. Withdrawal not possible.")

    def check_balance(self):
        return self.account_balance

# Create an instance of the Account class
my_account = Account(account_number="1774284044", account_balance=100000000.0, account_holder="Folarin")

# Deposit $500 into the account
my_account.deposit(20500.0)

# Check the current balance
print("Current balance:", my_account.check_balance())

# Withdraw $300 from the account
my_account.withdraw(300.0)

# Check the current balance after withdrawal
print("Current balance after withdrawal:", my_account.check_balance())
