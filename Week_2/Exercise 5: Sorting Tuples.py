# Exercise 5: Sorting Tuples

# Create a list of tuples named students where each tuple contains a student's name and their score: [('Alice', 85), ('Bob', 90), ('Charlie', 80)]

students = [('Alice', 85), ('Bob', 90), ('Charlie', 80)]

# Sort the list of tuples based on the students' scores in descending order.
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
# Print the sorted list.

print("Sorted list of students based on scores:")
print(sorted_students)
