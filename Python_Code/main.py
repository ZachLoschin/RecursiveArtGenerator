# Library Imports
import turtle as t
import FunctionDefs as my

"""
Zachary Loschinskey
7/24/2022
Description: Script to recursively draw a tree to create fun art!
"""

if __name__ == "__main__":

    # Create the window
    wn = t.Screen()
    wn.bgcolor("white")
    wn.title("Turtle")

    # Create turtle object
    # jacky = t.Turtle(visible=True)

    my.draw_branch(x=0, y=-400, angle=90, depth=0, width=10, length=200)

    # End turtle actions
    t.done()
