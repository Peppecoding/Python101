# Task 2 - Mini Calculator

# Ask the user for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Choose the operation (Add, Subtract, Multiply, Divide): ").lower()

# Perform the chosen operation and handle divide by zero error
if operation == "add":
    result = number1 + number2
elif operation == "subtract":
    result = number1 - number2
elif operation == "multiply":
    result = number1 * number2
elif operation == "divide":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation selected"

# Display the result
print(f"Result: {result}")
