# Create a dictionary named students with each key as a student's name
students = {
    'Alice': {'age': 22, 'grade': 'A'},
    'Bob': {'age': 23, 'grade': 'B'},
    'Charlie': {'age': 21, 'grade': 'C'}
}

# Write a loop to print out each student's name, age, and grade
for student_name, info in students.items():
    print(f"Student: {student_name}, Age: {info['age']}, Grade: {info['grade']}")
