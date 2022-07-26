import turtle as t
import random as rand
import numpy as np

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


def draw_branch(x, y, angle, depth, width, length, color):
    # Function to draw a tree branch given a sta, srting location
    turtle = t.Turtle(visible=False)
    turtle.speed(0)

    # Ensure pen is up and go to start location
    turtle.penup()
    turtle.goto(x, y)

    if depth <= 6:

        if width <= 0:
            width = 3

        if length <= 15:
            length = 15

        # Ensure turtle is facing north
        turtle.setheading(angle)

        # Draw the stem of the tree
        turtle.color(color)
        turtle.width(width)
        turtle.pendown()
        turtle.forward(length)

        # Redefine lengths
        newLength = length - 20

        array = np.zeros(3)
        map(color, array)
        array[0] = rand.randint(1, 10) / 10
        array[1] = rand.randint(1, 10) / 10
        array[2] = rand.randint(1, 10) / 10

        newColor = tuple(array)
        # Recursively call branches
        draw_branch(turtle.xcor(), turtle.ycor(), depth=depth+1,
                    width=width-5, length=newLength, angle=angle+15, color=newColor)

        draw_branch(turtle.xcor(), turtle.ycor(), depth=depth+1,
                    width=width-5, length=newLength, angle=angle-15, color=newColor)

        draw_branch(turtle.xcor(), turtle.ycor(), depth=depth + 1,
                    width=width-5, length=newLength, angle=angle, color=newColor)

        # # Draw leaves
        # topX = turtle.xcor()
        # topY = turtle.ycor()
        # draw_leaf(topX + 5, topY, turtle)













