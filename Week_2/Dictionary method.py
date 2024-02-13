# Define the dictionary as provided in the example
student = {
    "name": "John",
    "age": 20,
    "subject": "Computer Science"
}

# Use keys() method
print(student.keys())

# Use values() method
print(student.values())

# Use items() method
print(student.items())

# Use get() method
print(student.get("name"))

# Use pop() method
print(student.pop("age"))

# After pop, the dictionary no longer contains 'age'
print(student)

# Use popitem() method
print(student.popitem())

# After popitem, the dictionary will have one less item
print(student)

# Use clear() method
student.clear()

# Now 'student' dictionary is empty
print(student)

# Redefine 'student' for the copy() example
student = {
    "name": "John",
    "age": 20,
    "subject": "Computer Science"
}

# Use copy() method
student_copy = student.copy()
print(student_copy)
