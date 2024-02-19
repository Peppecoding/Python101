class Rectangle:
    # Constructor: Initializes a new instance of the Rectangle class
    def __init__(self, width, height):
        # The constructor takes two parameters: width and height, and assigns them to the instance variables
        self.width = width
        self.height = height

    # Getter for width: Allows us to retrieve the width of the rectangle
    def get_width(self):
        # Simply returns the value of the instance variable width
        return self.width

    # Setter for width: Allows us to set the width of the rectangle
    def set_width(self, width):
        # Takes a new width value and updates the instance variable
        self.width = width

    # Getter for height: Allows us to retrieve the height of the rectangle
    def get_height(self):
        # Simply returns the value of the instance variable height
        return self.height

    # Setter for height: Allows us to set the height of the rectangle
    def set_height(self, height):
        # Takes a new height value and updates the instance variable
        self.height = height

    # Method to calculate and print the area of the rectangle
    def print_area(self):
        # Calculates the area by multiplying width and height
        area = self.width * self.height
        # Prints the area
        print(f"The area of the rectangle is: {area}")

# Example usage:
rect = Rectangle(10, 20)  # Create a rectangle with width 10 and height 20

# Get the width and height
print("Initial width:", rect.get_width())
print("Initial height:", rect.get_height())

# Set new values for width and height
rect.set_width(30)
rect.set_height(40)

# Get the updated width and height
print("Updated width:", rect.get_width())
print("Updated height:", rect.get_height())

# Print the area of the rectangle
rect.print_area()
