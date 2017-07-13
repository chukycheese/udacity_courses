import turtle

def draw_square():

    # Setting a window with the background colored red
    window = turtle.Screen()
    window.bgcolor('red')

    # Move a turtle named brad forward
    brad = turtle.Turtle()

    # Customize the turtle
    brad.shape("turtle")
    brad.color('yellow')
    brad.speed(2)

    # Turn Brad right 90 degrees and move forward

    brad.forward(100)

    brad.right(90)
    brad.forward(100)

    brad.right(90)
    brad.forward(100)

    brad.right(90)
    brad.forward(100)

    # Add another tutle named angie
    angie = turtle.Turtle()

    # Customize angie
    angie.shape(name='arrow')
    angie.color('blue')

    # angie, draw a circle
    angie.circle(100)

    window.exitonclick()

draw_square()
