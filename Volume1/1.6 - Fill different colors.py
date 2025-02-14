#Task:- Fill colour in the second circle using begin_fill and the end_fill.
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("red")
# Set the color to green
t.color("green")
# Begin to fill color
t.begin_fill()
t.circle(80)
# End-filling color
t.end_fill()
t.color("red")

t.circle(50)

turtle.done()
