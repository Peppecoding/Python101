# Base Class
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Method to show the details of an instance of the Employee class
    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Email: {self.email}")

# Create a class called programmer thatn inherits from the Employee class
# Inherit from the Employee class
        
# Derived Class
class Programmer(Employee):
    # Inheriting from the Employee class
    def __init__(self, name, email, programming_languages):
        super().__innit__(name,email)
        self.programming_languages = programming_languages

    # Method to show details of the Programmer class
    def show_details(self):
        # Call the show_details method of the base class
        super().show_details()
        # Additional information specific to Programmer
        print(f"Programming Languages: {self.programming_languages}")

    # Getter method for programming_languages
    def get_programming_languages(self):
        return self.programming_languages

    # Setter method for programming_languages
    def set_programming_languages(self, programming_languages):
        self.programming_languages = programming_languages

# Creating an instance of Programmer
programmer = Programmer("Alice", "alice@example.com", ["Python", "Java"])

# Display the details before update
print("Before update:")
programmer.show_details()

# Updating the programming languages using the setter method
programmer.set_programming_languages(["Python", "Java", "C++"])

# Display the updated information
print("\nAfter update:")
programmer.show_details()
