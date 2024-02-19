class Rectangle:
    # Constructor
    def __init__(self, width, height):
        # The attributes are declared with a single underscore, indicating they are 'protected' 
        # and should not be accessed directly outside of class methods.
        self._private_width = width
        self._private_height = height

    # Getter for height
    def get_height(self):
        # This method allows safe retrieval of the height attribute.
        return self._private_height

    # Getter for width
    def get_width(self):
        # This method allows safe retrieval of the width attribute.
        return self._private_width

    # Setter for height
    def set_height(self, newHeight):
        # This method allows safely setting the value of the height attribute.
        self._private_height = newHeight

    # Setter for width
    def set_width(self, newWidth):
        # This method allows safely setting the value of the width attribute.
        self._private_width = newWidth

    # Method to calculate and print the area
    def calculate_area(self):
        # This method calculates the area based on the 'private' attributes.
        print(f"Area of Rectangle is {self._private_width * self._private_height}")


rect = Rectangle(10, 20)  # Create a rectangle with width 10 and height 20

# Get the width and height
print("Initial width:", rect.get_width())
print("Initial height:", rect.get_height())


