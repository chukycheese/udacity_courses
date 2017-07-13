import turtle

# Draw a flower
def draw_leaf(some_turtle):

    for i in range(2):
        some_turtle.forward(100)
        some_turtle.right(30)
        some_turtle.forward(100)
        some_turtle.right(150)

def draw_flower():
    window = turtle.Screen()

    ted = turtle.Turtle()
    ted.shape('turtle')
    ted.color('blue')
    ted.speed(20)

    for i in range(36):
        draw_leaf(ted)
        ted.right(10)

    ted.right(90)
    ted.forward(400)

    window.exitonclick()

# draw_flower()

# Draw a fractal

# Draw initials
