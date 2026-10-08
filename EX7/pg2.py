class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        # Add salaries
        return self.salary + other.salary

    def __sub__(self, other):
        # Subtract salaries
        return self.salary - other.salary

    def __mul__(self, other):
        # Multiply salaries
        return self.salary * other.salary

    def __eq__(self, other):
        # Compare salaries
        return self.salary == other.salary

    def __str__(self):
        return f"Employee(name={self.name}, salary={self.salary})"

# Example usage
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(f"{emp1} + {emp2} = {emp1 + emp2}")
print(f"{emp1} - {emp2} = {emp1 - emp2}")
print(f"{emp1} * {emp2} = {emp1 * emp2}")
print(f"{emp1} == {emp2} : {emp1 == emp2}")
print(f"{emp1} == Employee('Alice', 50000): {emp1 == Employee('Alice', 50000)}")

