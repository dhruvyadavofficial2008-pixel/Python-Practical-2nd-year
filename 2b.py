
nested_tuple = (
    ("Data Structures", 101),
    ("Database Management System", 103),
    ("Computer Networks", 102)
)


sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])


print("Sorted Subjects (by subject code):", sorted_subjects)
