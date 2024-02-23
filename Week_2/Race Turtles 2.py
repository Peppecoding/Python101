import turtle
import random

# Create the screen
screen = turtle.Screen()
screen.title("Turtles Racing")
screen.bgpic("/Users/giuseppemendoza/Documents/Bootcamp/Screenshot 2024-02-13 at 13.33.35.png")

# Create two turtle instances
peppe = turtle.Turtle()
bob = turtle.Turtle()

# Set the colors
peppe.color("red")
bob.color("blue")

# Set the shapes
peppe.shape("turtle")
bob.shape("turtle")

# Increase the size of the turtles
peppe.shapesize(3)
bob.shapesize(2)

# Move the turtles to their starting point
peppe.penup()
peppe.goto(-160, 100)
peppe.pendown()

bob.penup()
bob.goto(-160, 40)
bob.pendown()

# Define the race distance
finish_line = 300

# Race
for movement in range(100):
    peppe.forward(random.randint(1, 5))
    bob.forward(random.randint(1, 5))

    # Check if any turtle has crossed the finish line
    if peppe.xcor() >= finish_line or bob.xcor() >= finish_line:
        break

# Determine the winner
if peppe.xcor() > bob.xcor():
    winner = "Peppe"
elif bob.xcor() > peppe.xcor():
    winner = "Bob"
else:
    winner = "It's a tie!"

# Print the winner's name
print("The winner is", winner)

# Keep the window open until it is clicked
screen.exitonclick()
