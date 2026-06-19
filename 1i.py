students = {
    "Shail": 85,
    "Dron": 92,
    "Krishna": 78,
    "Dhruv": 88,
    "Abhay": 95
}

print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)
print("\nClass Average:", average)

top_student = max(students, key=students.get)
print("Highest Marks Scored By:", top_student)
print("Marks:", students[top_student])
