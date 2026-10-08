class BankCustomer:
    def __init__(self, name, account_number, initial_balance):
        self.name = name
        self.account = self.BankAccount(account_number, initial_balance)
   
    def show_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.account.account_number}")
        print(f"Account Balance: {self.account.balance}")

    class BankAccount:
        def __init__(self, account_number, balance):
            self.account_number = account_number
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited {amount}. New balance is {self.balance}.")
            else:
                print("Deposit amount must be positive.")

        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Withdrawal amount exceeds balance or is invalid.")

        def get_balance(self):
            return self.balance

customer1 = BankCustomer("John Doe", "123456789", 10000)
customer1.show_details()
customer1.account.deposit(5000)
customer1.account.withdraw(2000)
customer1.show_details()
