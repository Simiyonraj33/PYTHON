# Base class 1
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")

# Base class 2
class Student:
    def __init__(self, student_id, course):
        self.student_id = student_id
        self.course = course

    def display_student(self):
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

# Derived class
class Intern(Employee, Student):
    def __init__(self, emp_id, name, student_id, course, duration):
        Employee.__init__(self, emp_id, name)
        Student.__init__(self, student_id, course)
        self.duration = duration

    def display_intern(self):
        self.display_employee()
        self.display_student()
        print(f"Internship Duration: {self.duration} months")

# Example usage
intern1 = Intern(101, "Alice", "S123", "Computer Science", 6)
intern1.display_intern()
