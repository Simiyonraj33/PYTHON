employees = {}
n = int(input("Enter the number of employees: "))
for i in range(n):
   name = input("Enter employee name: ")
   salary = int(input("Enter employee salary: "))
   employees[name] = salary
print("\nEmployees with salary greater than 50000:")
for name, salary in employees.items():
   if salary > 50000:
      print(name)
