# learn and using stings, integer, float boolean

#Data Types
#String "Hello World" and add [number starting from 0]
print("Hello"[4])

#integer
print(3 + 2)

#float is a number with decimal place
print(3 + 2.5 * 6)

#boolean
print(True)
print(False)

num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters")

# Body mass calculator

height = input("What is you height\n")
weight = input("What is your weight\n")

print(height/weight)


# PEMDAS stands for Parentheses, Exponents, Multiplication and Division (same level), and Addition and Subtraction (same level)


# Define x before converting it to an integer
x = "10"  # Assuming x is a string that can be converted to an integer
x = int(x)
print("x", type(x), x)  # This will output the type of x and its value

# PIN NUMBER

while True:
    try:
        pin_number = int(input("Please enter your pin number: "))
        print(f"The entered pin number is {pin_number}.")
        break  # Exit the loop if the input is an integer
    except ValueError:
        print("That's not an integer! Please enter only numbers.")

# Transform string to int
x = "5"
y = "10"
print(int(x) + int(y))


# Converted string to int
x = "5"
y = "10"
print(int(x) + int(y))

# Removed the quote
x = 5
y = 10
print(x+y)

# Convert the vaiable data type string  into  integer
x = int("5")
y = int("10")
print(x+y)

# Float Bank tranfer
amount = float(input("Please enter the total amount of bank transfer: "))
print(f"Your bank transfer is {amount}.")

# string  doule quote

test = " I like \"Monty Python\""
print(test)
age = 43
test1= f"I am {age} year old, next year it will be {age+1}"
print(test1)

# Boolean is a TRUE and FALSE value  and the computer read it as False = 0 and True = 1

print(True>False)
print(True<False)


# other

x = "Hello World"
print(len(x))
print(x.upper())
print(x.lower())
print(x.endswith("d"))