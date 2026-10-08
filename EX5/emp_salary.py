class EmployeeSalary:
    def __init__(self, n, bp):
        self.n = n
        self.bp = bp
        self.hra=float(input("enter the \'hra\' percentage :"))
        self.allow=1000
    def calc(self):
        hra = (self.hra/ 100) * self.bp
        tot = self.bp + hra + self.allow
        return tot
    def disp(self):
        tot=self.calc()
        hra = (self.hra / 100) * self.bp
        print("\nTotal salary for ",self.n,"\t: Rs. ",tot,"\nBasic Pay: Rs. ",self.bp,"\nHRA: Rs. ",hra,"\nAllowance: Rs.",self.allow,"\n")
n = input("Enter the employee's name: ")
bp = float(input("Enter the basic pay: Rs. "))
e= EmployeeSalary(n, bp)
e.disp()
