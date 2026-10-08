# Base class
class Hospital:
    def __init__(self, name):
        self.name = name

    def show_hospital(self):
        print(f"Hospital Name: {self.name}")

# First derived class
class Department(Hospital):
    def __init__(self, name, department_name):
        super().__init__(name)
        self.department_name = department_name

    def show_department(self):
        print(f"Department: {self.department_name}")

# Second derived class (multi-level inheritance)
class Doctor(Department):
    def __init__(self, name, department_name, doctor_name):
        super().__init__(name, department_name)
        self.doctor_name = doctor_name

    def show_doctor(self):
        print(f"Doctor: {self.doctor_name}")

# Object creation and usage
d = Doctor("City Hospital", "Cardiology", "Dr. John Smith")
d.show_hospital()
d.show_department()
d.show_doctor()
