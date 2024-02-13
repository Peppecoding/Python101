import turtle  # Import the turtle module for creating graphics
import random  # Import the random module for generating random numbers

# Create the screen
screen = turtle.Screen()  # Create a turtle screen object
screen.title("Turtles Racing")  # Set the title of the screen
screen.bgpic("/Users/giuseppemendoza/Documents/Bootcamp/Screenshot 2024-02-13 at 13.33.35.png")  # Set the background color bgpic( for picture png) and bgcolor ("rYellow") of the screen to light green
# Note: The turtle and random modules are part of Python's standard library, so you can find them in the Python documentation.

# Create two turtle instances
peppe = turtle.Turtle()  # Create a turtle object named 'john'
bob = turtle.Turtle()   # Create another turtle object named 'bob'

# Set the colors
peppe.color("red")  # Set John's color to red if is fillcolor it add the line black around the draw ( lo de linea y es formato negro el deliniado)
bob.color("blue")  # Set Bob's color to blue

# Set the shapes
peppe.shape("turtle")  # Set John's shape to turtle
bob.shape("turtle")   # Set Bob's shape to turtle

# Increase the size of the turtles
peppe.shapesize(2)  # Increase the size of John's turtle
bob.shapesize(2)   # Increase the size of Bob's turtle

# Move John to a different starting point
peppe.penup()    # Lift John's pen
peppe.goto(-160, 100)  # Move John to coordinates 
peppe.pendown()  # Place John's pen down

# Move Bob to a different starting point
bob.penup()    # Lift Bob's pen
bob.goto(-160, 50)  # Move Bob to coordinates
bob.pendown()  # Place Bob's pen down

# Define the race distance
finish_line = 300  # Set the x-coordinate position of the finish line

# Race!
for movement in range(100):  # Loop to simulate the race for 100 movements
    peppe.forward(random.randint(1, 5))  # John moves forward a random distance between 1 and 5 units (https://www.geeksforgeeks.org/turtle-programming-python/)
    bob.forward(random.randint(1, 5))   # Bob moves forward a random distance between 1 and 5 units

    # Check if any turtle has crossed the finish line
    if peppe.xcor() >= finish_line or bob.xcor() >= finish_line:
        break

# Determine the winner
if peppe.xcor() > bob.xcor():
    winner = "Peppe"  # John wins if he crossed the finish line first
elif bob.xcor() > peppe.xcor():
    winner = "Bob"   # Bob wins if he crossed the finish line first
else:
    winner = "It's a tie!"  # It's a tie if both turtles are at the same position

# Print the winner's name
print("The winner is", winner)

# Keep the window open until it is clicked
screen.exitonclick()  # Keeps the window open until clicked, allowing the user to view the result before closing
