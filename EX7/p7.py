# Base class
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Base Salary: {self.base_salary}")

# Subclass 1: Full-time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

# Subclass 2: Part-time Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, hours_worked, rate_per_hour):
        super().__init__(name, emp_id, base_salary)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.base_salary + (self.hours_worked * self.rate_per_hour)

# Example usage
ft_emp = FullTimeEmployee("Alice", 101, 30000, 5000)
pt_emp = PartTimeEmployee("Bob", 102, 10000, 20, 200)

print("Full-Time Employee Salary:")
ft_emp.display_info()
print("Total Salary:", ft_emp.calculate_salary())

print("\nPart-Time Employee Salary:")
pt_emp.display_info()
