class Emp:
    def __init__(self, emp_n, emp_sal):
        self.emp_n = emp_n
        self.emp_sal = emp_sal

    def method1(self):
        print(self.emp_n)
        print('Salary:', self.emp_sal)

    def method2(self):
        if self.emp_sal >= 80000:
            print('Grade Pay 8')
        elif self.emp_sal >= 70000:
            print('Grade Pay 7')
        elif self.emp_sal >= 60000:
            print('Grade Pay 6')
        else:
            print('CONSOLIDATED')

n = int(input('Enter Number of Emp: '))
for i in range(n):
    emp_n = input('Enter Name: ')
    emp_sal = int(input('Enter Salary: '))
e = Emp(emp_n, emp_sal)
e.method1()
e.method2()
print()
