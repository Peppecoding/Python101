# Task 1 - Personal Information
# Ask for name and age, then print.
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Hello, {name}! You are {age} years old.")

# Assuming 1 human year is equivalent to 7 dog years
dog_years = age * 7
print(f"Hello, {name}! You are {age} years old. That's {dog_years} in dog years!")
