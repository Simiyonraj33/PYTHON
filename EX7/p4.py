class EmployeeInfo:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def display_info(self):
        print("Employee Information:")
        print("---------------------")
        print("Name: ", self.name)
        print("Employee ID: ", self.emp_id)
        print("Base Salary: ₹", self.base_salary)

class Allowances(EmployeeInfo):  # Inheriting from EmployeeInfo
    def __init__(self, name, emp_id, base_salary, hra, da, ta):
        super().__init__(name, emp_id, base_salary)
        self.hra = hra
        self.da = da
        self.ta = ta

    def total_allowances(self):
        return self.hra + self.da + self.ta

class SalaryCalculator(Allowances):  # Inheriting from Allowances
    def __init__(self, name, emp_id, base_salary, hra, da, ta, pf, tax):
        super().__init__(name, emp_id, base_salary, hra, da, ta)
        self.pf = pf
        self.tax = tax

    def total_deductions(self):
        return self.pf + self.tax

    def calculate_net_salary(self):
        gross_salary = self.base_salary + self.total_allowances()
        net_salary = gross_salary - self.total_deductions()
        return net_salary

    def display_salary_slip(self):
        self.display_info()
        print("Total Allowances: ₹", self.total_allowances())
        print("Total Deductions: ₹", self.total_deductions())
        print("Net Salary: ₹", self.calculate_net_salary())

# Getting user input and running the program
e = SalaryCalculator(
    input("Enter the name of the employee: "),
    input("Enter the employee ID: "),
    float(input("Enter the base salary: ")),
    float(input("Enter the HRA: ")),
    float(input("Enter the DA: ")),
    float(input("Enter the TA: ")),
    float(input("Enter the PF: ")),
    float(input("Enter the tax: "))
)
e.display_salary_slip()
