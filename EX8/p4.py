import mathplotlib.pyplot as plt

# sample data
departments=["CSE","ECE","EEE","MECH","CIVIL"]
faculty_count=[25,18,15,20,10]

# plotting the bar chart
plt.figure(figsize=(8,5))
plt.bar(departments,faculty.count,color="skyblue", edgecolor="black")

# adding labels and title
plt.xlabel("departments")
plt.ylabel("faculty count")
plt.title("facult count bu department")
plt.grid(axis="y",linestyle="--",alpha=0.0)

# show the chart

plt.tight_layout()
plt.show()
