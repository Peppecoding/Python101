# Examples of FUNCTIONS
def bootcamp_welcome(day="some day"):
    print("Welcome to the Bootcamp")
    print(f"This is day {day}")

print("Not part of the function")

bootcamp_welcome()  # This will use the default value for day.
bootcamp_welcome(3)

# Parameters

# Function definition
def bootcamp_welcome(bootcamp_subject):
    print(f"Welcome to the {bootcamp_subject} Bootcamp!")

# Calling the function with the arguments
bootcamp_welcome("Data Analytics")
bootcamp_welcome("Cyber Security")

#  other example

def cash_machine(acc_num, sort_code, amount):
    print(f"Withdrawing £{amount}\nAccount Number: {acc_num}\nSort Code: {sort_code}")

# Call the function with the provided arguments
cash_machine(1234556, 304055, 250)

# Function to create a birthday message
def birthday_message(name, age):
    print(f"\nHappy Birthday {name}! I hear you are {age} today!\n")

# Function to output a drinks order
def drinks_order(size, drink_type):
    print(f"\nOne {size} {drink_type}, coming right up!\n")


birthday_message("Giuseppe", 25)
drinks_order("large", "Mocha")


# Initialize a global variable for the order count
order_count = 0

def take_order(topping, Topping1, Topping2):
    global order_count  # We use global in Python to refer to a variable outside the function
    order_count += 1
    print(f"\nPizza with {topping}, {Topping1}, and {Topping2}\n")
    print(f"Order count is now: {order_count}\n")

# Example call to the function with three toppings
take_order("sweetcorn", "mushrooms", "pepperoni")

#  Object Oriented Python Programming

# Define a function to simulate a cash machine
def cash_machine(user_pin, requested_amount):
    # These are example values. In a real scenario, these would be securely handled and stored.
    correct_pin = 1234
    balance = 1000  # Starting balance, for example purposes

    # Check if the entered pin is correct
    if user_pin == correct_pin:
        # Check if there's enough money in the account
        if requested_amount <= balance:
            # Dispense cash and show new balance
            balance -= requested_amount
            print(f"\nCash dispensed: £{requested_amount}. \nNew balance: £{balance}.")
        else:
            print("Sorry, insufficient funds.")
    else:
        print("Incorrect PIN. Please try again.")

# Example usage of the cash machine function
cash_machine(user_pin=1234, requested_amount=100000)

#LIST # My Favourite movies
my_movies = ["Star Wars", "Super Mario", "Avatar"]
print(my_movies)

print(len(my_movies))

my_movies.append("Fast and Furius")

print(my_movies)

my_movies.pop()
print(my_movies)

# Negative Indexing:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# Example: printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'



# Tuple

example_tuple = ('apple', 'banana', 'cherry') # Can't be change is immutable

example_set = {'apple', 'banana', 'cherry', 'apple'}  # 'apple' is a duplicate and will be removed.
example_set.add('orange')  # Adding an element
example_set.remove('banana')  # Removing an element


example_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
example_dict['age'] = 31  # Changing the value associated with key 'age'
example_dict['country'] = 'USA'  # Adding a new key-value pair
del example_dict['city']  # Removing the key 'city' and its associated value

print(example_dict)


list_of_numbers = [1,3,5,2,4]
list_of_numbers.sort()

for each_number in list_of_numbers:
    print(each_number)

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in num_list:
    if i % 2 == 0:
        print(f"{i} is even")
    elif i % 2 != 0:
        print(f"{i} is odd")
    elif i == 5:
        print("ENDING")
        break

    num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
