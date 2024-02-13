import turtle


def draw_shape_with_color(sides, color):
    angle = 360 / sides  # Calculate the angle of turn based on the number of sides
    turtle.fillcolor(color)  # Set the fill color for the shape
    turtle.begin_fill()  # Begin filling the shape with color
    for _ in range(sides):  # Draw each side of the shape
        turtle.forward(100)  # Move forward by 100 units
        turtle.right(angle)  # Turn right by the calculated angle
    turtle.end_fill()  # Complete the filling process

draw_shape_with_color(8, "red")  # Example: Drawing an octagon filled with red color
turtle.done()  # Ends the turtle drawing session

