class InsufficientFundsException(Exception):
    def __init__(self, message="Withdrawal failed! Insufficient funds."):
        self.message = message
        #Exception.__init__(self,message)
class MinimumBalanceException(Exception):
    def __init__(self, message="Withdrawal failed! Minimum balance Rs.500 required"):
        self.message = message
        #Exception.__init__(self,message)
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited Rs.", amount)
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException()
        elif (self.balance - amount) < 500:
            raise MinimumBalanceException()
        else:
            self.balance -= amount
            print("Withdrawn Rs.", amount)  
    def check_balance(self):
        print("Current balance is Rs.", self.balance)
try:
    print("\n\nYRV Banking...\n Enter Details:")
    a = BankAccount(int(input("Enter Acc no:")), input("Enter name:"), int(input("Enter Amount:")))
except ValueError as e:
        print("Error:", e)
while True:
    try:
        print("1.Check Balance\n2.Deposit Amount\n3.Withdraw amount\n")
        ch=int(input("Enter your choice:"))
        if ch==1:
            a.check_balance()
        elif ch==2:
            a.deposit(int(input("Enter deposit amount:")))
        elif ch==3:
            a.withdraw(int(input("Enter withdraw amount:")))
        else:
            print("Invalid Input . Try Again")
        ch=(input("Wanna Continue...?(Yes/No):"))
        if ch.lower()=="no":
           print("Happie Banking...:)")
           break
    except InsufficientFundsException as e:
        print(e.message)  
    except MinimumBalanceException as e:
        print(e.message)
    except Exception as e:
        print("An error occurred:", e)

