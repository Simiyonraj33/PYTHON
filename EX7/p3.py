class Person:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)
class Student(Person):
    def __init__(self, name, student_id,m1,m2,m3):
        super().__init__(name)
        self.student_id = student_id
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def total_marks(self):
        return self.m1 + self.m2 + self.m3
    def average_marks(self):
        return self.total_marks() / 3
    def display_info(self):
        super().display_name()
        print("Student ID:", self.student_id)
        print("Marks in Subject 1:", self.m1)
        print("Marks in Subject 2:", self.m2)
        print("Marks in Subject 3:", self.m3)
        print("Total Marks:", self.total_marks())
        print("Average Marks:", self.average_marks())
class Graduate(Student):
    def __init__(self, name, student_id,m1,m2,m3,degree):
        super().__init__(name, student_id,m1,m2,m3)
        self.degree = degree
    def check_eligibility(self):
        if self.average_marks() >= 60:
            print(f"Eligible for graduation of {self.degree} degree")
        else:
            print(f"Not eligible for graduation of {self.degree} degree")
    def display_full_info(self):
        print("Graduate Information:")
        print("---------------------")
        super().display_info()
        print("Degree:", self.degree)
        self.check_eligibility()
g= Graduate(input("Enter the name of the student: "), input("Enter the student ID: "), int(input("Enter marks in subject 1: ")), int(input("Enter marks in subject 2: ")), int(input("Enter marks in subject 3: ")), input("Enter the degree: "))
g.display_full_info()
