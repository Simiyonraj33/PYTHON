class NegativeValueError(Exception):
   def __init__(self, message="Error: Amount cannot be negative!"):
      self.message = message
class InvalidDaysError(Exception):
   def __init__(self, message="Error: Number of days must be between 1 and 31!"):
      self.message = message   
class mess_bill:
   def __init__(self,cpd,dp,dt,ec):
      self.cpd=cpd
      self.dp=dp
      self.dt=dt
      self.ec=ec
      self.cdt=50
   def disp(self):
      total_fees = (self.cdt* self.dt)+(self.cpd*self.dp) + self.ec
      print("Total mess fees is Rs.", total_fees)
try:
    print("Mess Bill Calculation")
    cost_per_day = input("Enter mess cost per day (in Rs.): ")
    if not cost_per_day.isdigit():
        raise ValueError("Error: Cost per day must be a positive number.")
    cost_per_day = int(cost_per_day)
    days_present = input("Enter number of days you were present: ")
    if not days_present.isdigit():
        raise ValueError("Error: Number of days must be a positive number.")
    days_present = int(days_present)
    days_taken = input("Enter number of days you have taken mess services: ")
    if not days_taken.isdigit():
        raise ValueError("Error: Number of days must be a positive number.")
    days_taken = int(days_taken)
    extra_charges = input("Enter additional charges (extra food/late fees) in Rs.: ")
    if not extra_charges.isdigit():
        raise ValueError("Error: Additional charges must be a positive number.")
    extra_charges = int(extra_charges)
    if cost_per_day < 0 or days_present < 0 or days_taken < 0 or extra_charges < 0:
        raise NegativeValueError()
    if days_taken < 1:
        raise InvalidDaysError()
    if days_present < days_taken:
        raise ValueError("Error: Days present cannot be more than days mess services taken.")
    bill=mess_bill(cost_per_day,days_present,days_taken,extra_charges)
    bill.disp()
except NegativeValueError as e:
    print(e.message)
except InvalidDaysError as e:
    print(e.message)
except ValueError as e:
    print(e)
except Exception as e:
    print("An unexpected error occurred:", e)

