import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():

    # Setting a window with the background colored red
    window = turtle.Screen()
    window.bgcolor('red')

    # Move a turtle named brad forward
    brad = turtle.Turtle()

    # Customize the turtle
    brad.shape("turtle")
    brad.color('yellow')
    brad.speed(2)

    for i in range(36):
        draw_square(brad)
        brad.right(10)

    # # Add another turtle named angie
    # angie = turtle.Turtle()
    #
    # # Customize angie
    # angie.shape(name='arrow')
    # angie.color('blue')
    #
    # # angie, draw a circle
    # angie.circle(100)
    #
    # # Add the third turtle named charles
    # charles = turtle.Turtle()
    #
    # # Customize charles
    # charles.shape(name='turtle')
    # charles.color('green')
    #
    # # charles, draw a triangle
    # for i in range(3):
    #     charles.back(100)
    #     charles.right(120)

    window.exitonclick()

draw_art()
