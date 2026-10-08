class Employee:
   def __init__(self,name):
      self.name=name
   def calculate_salary(self):
      return "Salary not defined for base employee"
   def display(self):
      print("Employee type: ",self.__class__.__name__)
      print("Name: ",self.name)
      print("Salary: ",self.calculate_salary())
class PartTimeEmployee(Employee):
   def __init__(self,name,hours,rate):
      super().__init__(name)
      self.hours=hours
      self.rate=rate
   def calculate_salary(self):
      return self.hours*self.rate
class FullTimeEmployee(Employee):
   def __init__(self,name,monthly_salary):
      super().__init__(name)
      self.monthly_salary=monthly_salary
   def calculate_salary(self):
      return self.monthly_salary
#Object creation
e1=Employee("Vishnu")
e2=PartTimeEmployee("rebin",20,200)
e3=FullTimeEmployee("mathew",50000)
e1.display()
e2.display()
e3.display()

