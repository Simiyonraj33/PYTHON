class Employee:
    def __init__(self, name, base_salary, bonus, deductions):
        self.name = name
        self.salary = self.salaryEmp(base_salary, bonus, deductions)

    def show_salary_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: {self.salary.base_salary}")
        print(f"Bonus: {self.salary.bonus}")
        print(f"Deductions: {self.salary.deductions}")
        print(f"Gross Salary: {self.salary.gross_salary()}")
        print(f"Net Salary: {self.salary.net_salary()}")
    class salaryEmp:
        def __init__(self, base_salary, bonus, deductions):
            self.base_salary = base_salary
            self.bonus = bonus
            self.deductions = deductions

        def gross_salary(self):
            return self.base_salary + self.bonus

        def net_salary(self):
            return self.gross_salary() - self.deductions
       
emp1=Employee("John Doe", base_salary=50000, bonus=5000, deductions=2000)
emp1.show_salary_details()
