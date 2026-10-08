class Person:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)
class Employee(Person):
    def __init__(self, name, emp_id, position):
        super().__init__(name)
        self.emp_id = emp_id
        self.position = position
    def display_emp_info(self):
        super().display_name()
        print("Employee ID:", self.emp_id)
        print("Position:", self.position)
class Student(Person):
    def __init__(self, name, student_id, grade):
        super().__init__(name)
        self.student_id = student_id
        self.grade = grade
    def display_student_info(self):
        super().display_name()
        print("Student ID:", self.student_id)
        print("Grade:", self.grade)
class Internship(Person):
    def __init__(self, name, emp_id, position, student_id, grade, research_topic, supervisor, duration):
        super().__init__(name)
        self.emp_id = emp_id
        self.position = position
        self.student_id = student_id
        self.grade = grade
        self.research_topic = research_topic
        self.supervisor = supervisor
        self.duration = duration
    def display_internship_info(self):
        print("\nInternship Information:")
        print("------------------------")
        self.display_name()
        print("Employee ID:", self.emp_id)
        print("Position:", self.position)
        print("Student ID:", self.student_id)
        print("Grade:", self.grade)
        print("Research Topic:", self.research_topic)
        print("Supervisor:", self.supervisor)
        print("Duration:", self.duration, "months\n")
i = Internship(
    input("Enter the name of the intern: "),
    input("Enter the employee ID: "),
    input("Enter the position: "),
    input("Enter the student ID: "),
    input("Enter the grade: "),
    input("Enter the research topic: "),
    input("Enter the supervisor's name: "),
    int(input("Enter the duration in months: "))
)
i.display_internship_info()
