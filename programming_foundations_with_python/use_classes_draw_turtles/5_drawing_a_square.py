import turtle

def draw_square():

    # Setting a window with the background colored red
    window = turtle.Screen()
    window.bgcolor('red')

    # Move a turtle named brad forward
    brad = turtle.Turtle()
    brad.forward(100)

    # Turn Brad right 90 degrees and move forward
    brad.right(90)
    brad.forward(100)

    brad.right(90)
    brad.forward(100)

    brad.right(90)
    brad.forward(100)

    window.exitonclick()

draw_square()
