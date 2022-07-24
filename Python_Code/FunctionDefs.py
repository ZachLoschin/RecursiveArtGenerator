import turtle as t
import random as rand


def draw_leaf(x, y, turtle):
    # Function to draw a circular leaf given locating location

    # Ensure pen is up and go to start location
    turtle.penup()
    turtle.width(5)
    turtle.goto(x, y)

    # Draw circle
    turtle.pendown()
    turtle.color("light green")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()


def draw_branch(x, y, angle, depth, width, length):
    # Function to draw a tree branch given a starting location
    turtle = t.Turtle(visible=False)
    turtle.speed(0)

    # Ensure pen is up and go to start location
    turtle.penup()
    turtle.goto(x, y)

    if depth <= 4:

        if width <= 0:
            width = 3

        if length <= 10:
            length = 10

        # Ensure turtle is facing north
        turtle.setheading(angle)

        # Draw the stem of the tree
        turtle.color("brown")
        turtle.width(width)
        turtle.pendown()
        turtle.forward(length)

        # Redefine lengths
        newLength = length - 50

        # Recursively call branches
        draw_branch(turtle.xcor(), turtle.ycor(), depth=depth+1,
                    width=width-5, length=newLength, angle=angle+35)

        draw_branch(turtle.xcor(), turtle.ycor(), depth=depth+1,
                    width=width-5, length=newLength, angle=angle-35)

        draw_branch(turtle.xcor(), turtle.ycor(), depth=depth + 1,
                    width=width-5, length=newLength, angle=angle)

        # # Draw leaves
        # topX = turtle.xcor()
        # topY = turtle.ycor()
        # draw_leaf(topX + 5, topY, turtle)













