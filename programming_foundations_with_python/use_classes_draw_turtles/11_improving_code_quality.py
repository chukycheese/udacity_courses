import turtle

def draw_shapes():

    # Setting a window with the background colored red
    window = turtle.Screen()
    window.bgcolor('red')

    # Move a turtle named brad forward
    brad = turtle.Turtle()

    # Customize the turtle
    brad.shape("turtle")
    brad.color('yellow')
    brad.speed(2)

    # Turn Brad right 90 degrees and move forward x 4
    for i in range(4):
        brad.forward(100)
        brad.right(90)

    # Add another turtle named angie
    angie = turtle.Turtle()

    # Customize angie
    angie.shape(name='arrow')
    angie.color('blue')

    # angie, draw a circle
    angie.circle(100)

    # Add the third turtle named charles
    charles = turtle.Turtle()

    # Customize charles
    charles.shape(name='turtle')
    charles.color('green')

    # charles, draw a triangle
    for i in range(3):
        charles.back(100)
        charles.right(120)

    window.exitonclick()

draw_shapes()
