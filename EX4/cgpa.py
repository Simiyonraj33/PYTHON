def calc_gpa(grds):
"""Calculate GPA based on grades."""
    points_map = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 0,
        'RA': 0
    }

    total_points = 0
    for grade in grds:
        total_points += points_map.get(grade, 0)

    return total_points / len(grds) if grds else 0.0

# Get the number of students
n = int(input("Enter the number of students: "))

# Initialize a list to store student details
students = []

# Get details for each student
for _ in range(n):
    name = input("Enter name: ")
    grds = []
    for i in range(1, 4):  # For 3 subjects
        grd = input(f"Enter grade for Subject {i} (O, A+, A, B+, B, RA): ").upper()
        grds.append(grd)

    gpa = calc_gpa(grds)
    students.append((name, grds, gpa))

# Sort students by GPA in descending order
students.sort(key=lambda x: x[2], reverse=True)

# Print the results with ranks
print("\nStudent GPA Results:")
print("Rank | Name   | Grades         | GPA")
print("-----------------------------------------")
rank = 1  # Initialize rank counter
for student in students:
    name, grds, gpa = student

    # Create a string for grades using join
    grades_str = ', '.join(grds)

    print(f"{rank:<4} | {name:<6} | {grades_str:<15} | {gpa:.2f}")
    rank += 1  # Increment rank counter
