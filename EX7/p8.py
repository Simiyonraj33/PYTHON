# Base class
class Hospital:
    def __init__(self, name):
        self.name = name

    def show_hospital(self):
        print(f"Hospital Name: {self.name}")

# First child class
class Department(Hospital):
    def __init__(self, name, department_name):
        super().__init__(name)
        self.department_name = department_name

    def show_department(self):
        print(f"Department: {self.department_name}")

# Second child class
class Doctor(Hospital):
    def __init__(self, name, doctor_name):
        super().__init__(name)
        self.doctor_name = doctor_name

    def show_doctor(self):
        print(f"Doctor: {self.doctor_name}")

# Object creation
dept = Department("City Hospital", "Pediatrics")
doc = Doctor("City Hospital", "Dr. Smith")

# Using methods
dept.show_hospital()
dept.show_department()

doc.show_hospital()
