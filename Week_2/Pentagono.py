import turtle

def draw_pentagon():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)  # 360/5 = 72 degrees for a pentagon

draw_pentagon()
turtle.done()
