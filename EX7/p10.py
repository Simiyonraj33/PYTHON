# Base class 1
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Base class 2
class Doctor:
    def __init__(self, doctor_id, specialization):
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display_doctor(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Specialization: {self.specialization}")

# Base class 3
class Patient:
    def __init__(self, patient_id, disease):
        self.patient_id = patient_id
        self.disease = disease

    def display_patient(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Disease: {self.disease}")

# Derived class using multiple inheritance
class HospitalRecord(Person, Doctor, Patient):
    def __init__(self, name, age, gender, doctor_id, specialization, patient_id, disease, ward):
        Person.__init__(self, name, age, gender)
        Doctor.__init__(self, doctor_id, specialization)
        Patient.__init__(self, patient_id, disease)
        self.ward = ward

    def display_record(self):
        print("=== Hospital Record ===")
        self.display_person()
        self.display_doctor()
        self.display_patient()
        print(f"Ward: {self.ward}")

# Example usage
record = HospitalRecord("John Doe", 40, "Male", "D001", "Cardiologist", "P123", "Heart Disease", "Ward A")
record.display_record()
