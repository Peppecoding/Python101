# Parent class definition
class Mammal():
    # Constructor is not explicitly defined here, so this class uses the default constructor.

    # A method of the parent class
    def walk(self):
        # When this method is called, it prints "Walking" to the console.
        print("Walking")

# Child class definition, inheriting from Mammal
class Dog(Mammal):
    # Method specific to the Dog class
    def bark(self):
        # When this method is called, it prints "Bark" to the console.
        print("Bark")

# Another child class definition, also inheriting from Mammal
class Cat(Mammal):
    # Method specific to the Cat class
    def meow(self):
        # When this method is called, it prints "Meow" to the console.
        print("Meow")

# Creating an instance (object) of the Dog class
dog = Dog()
# Calling the walk method inherited from the Mammal class
dog.walk()   # This will print "Walking"
# Calling the bark method defined in the Dog class
dog.bark()   # This will print "Bark"

# The following line would raise an AttributeError, because the 'Dog' class does not have a 'meow' method
# dog.meow()
