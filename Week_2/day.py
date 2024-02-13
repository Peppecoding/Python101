import turtle
import random  # Import the random module

# Create the screen
screen = turtle.Screen()
screen.title("Turtles Racing")

# Set the background color
screen.bgcolor("lightgreen")

# Create two turtle instances
john = turtle.Turtle()
bob = turtle.Turtle()

# Set the colors
john.color("red")
bob.color("blue")

# Set the shapes
john.shape("turtle")
bob.shape("turtle")

# Move John to a different starting point
john.penup()
john.goto(-160, 100)
john.pendown()

# Move Bob to a different starting point
bob.penup()
bob.goto(-160, 70)
bob.pendown()

# Define the race distance
finish_line = 300

# Race!
for movement in range(100):
    john.forward(random.randint(1, 5))
    bob.forward(random.randint(1, 5))

    # Check if any turtle has crossed the finish line
    if john.xcor() >= finish_line or bob.xcor() >= finish_line:
        break

# Determine the winner
if john.xcor() > bob.xcor():
    winner = "John"
elif bob.xcor() > john.xcor():
    winner = "Bob"
else:
    winner = "It's a tie!"

# Print the winner's name
print("The winner is", winner)

# Keep the window open until it is clicked
screen.exitonclick()

