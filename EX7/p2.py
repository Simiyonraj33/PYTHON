class Account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def display_info(self):
        print("Account Information:")
        print("---------------------")
        print("Account Holder: ",self.account_holder)
        print("Account Number: ",self.account_number)
        print("Balance: ",self.balance)
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ",amount)
        print("New Balance: ",self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrawn: ",amount)
            print("New Balance: ",self.balance)
class SavingsAccount(Account):
    def __init__(self, account_holder, account_number, balance, interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print("Interest: ",interest)
        return interest
s= SavingsAccount(input("Enter the name of the account holder: "), input("Enter the account number: "), float(input("Enter the balance: ")), float(input("Enter the interest rate: ")))
s.calculate_interest()
s.deposit(float(input("Enter the amount to deposit: ")))
s.withdraw(float(input("Enter the amount to withdraw: ")))
s.display_info()
s.calculate_interest()
