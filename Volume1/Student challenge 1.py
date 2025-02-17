import turtle

# Create turtle object
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")

# Create flowers
t.circle(60)
t.left(60)
t.circle(60)
t.left(60)
t.circle(60)
t.left(60)
t.circle(60)
t.left(60)
t.circle(60)
t.left(60)
t.circle(60)
t.left(60)

# Create stem
t.color("green")
t.right(90)
t.forward(250)


# Create pot
t.color("brown")
t.begin_fill()
t.right(90)
t.forward(60)
t.right(90)
t.forward(80)
t.right(90)
t.forward(120)
t.right(90)
t.forward(80)
t.right(90)
t.forward(60)
t.end_fill()

# Create sun
t.color("yellow")
t.penup()
t.right(90)
t.forward(450)
t.right(90)
t.forward(200)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()


# Finish
turtle.done()
