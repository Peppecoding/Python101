import turtle

def race_winner():
    screen = turtle.Screen()  # Set up the screen
    screen.setup(500, 500)  # Define the size of the screen

    turtle1 = turtle.Turtle()  # Create the first turtle
    turtle2 = turtle.Turtle()  # Create the second turtle

    # Set up the turtles
    turtle1.color("blue")  # Color of the first turtle
    turtle2.color("green")  # Color of the second turtle

    turtle1.penup()  # Lift the pen up, so it doesn't draw while moving to start position
    turtle2.penup()
    turtle1.goto(-200, 20)  # Set the start position for the first turtle
    turtle2.goto(-200, -20)  # Set the start position for the second turtle
    turtle1.pendown()  # Put the pen down to start drawing
    turtle2.pendown()

    while True:  # Infinite loop to move the turtles
        turtle1.forward(10)  # Move the first turtle forward by 10 units
        turtle2.forward(10)  # Move the second turtle forward by 10 units

        # Check if any turtle has crossed the finish line
        if turtle1.xcor() >= 200:  # xcor() gives the x-coordinate of the turtle
            print("Blue turtle wins!")
            break
        elif turtle2.xcor() >= 200:
            print("Green turtle wins!")
            break

    screen.clear()  # Clear the screen after the race is over

race_winner()
