# Accessing and Modifying Dictionaries


# Accessing and Modifying Dictionaries:
# Create a dictionary named student with keys 'name', 'age', and 'grade'. Assign corresponding values for each key.
# Print out the student's name.
# Update the student's age to a new value and print the updated value, then the updated dictionary.

# Create a dictionary named student
student = {
    'name': 'Alice',
    'age': 21,
    'grade': 'A'
}

# Print out the student's name
print("Student's name:", student['name'])

# Update the student's age to a new value and print the updated value, then the 
student['age'] = 22
print("Updated age:", student['age'])

# uUpdated dictionary
print("Updated student dictionary:", student)