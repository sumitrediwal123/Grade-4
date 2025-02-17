import turtle
t=turtle.Turtle()


t.begin_fill()  #white box
t.color('white')
t.forward(200)
t.left(90)
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()

t.begin_fill() #green box
t.color('green')
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()


t.penup() # turtle for home point
t.goto(200, 40)
t.pendown()

t.begin_fill() #orange box
t.color('orange')
t.forward(40)
t.left(90)
t.forward(200)
t.left(90)
t.forward(40)
t.end_fill()


t.penup() #middle blue circle
t.home()
t.forward(100)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(20)

t.left(90)
t.forward(40)

t.backward(20)
t.left(90)
t.forward(20)
t.backward(40)
t.forward(20)
t.left(45)
t.forward(20)
t.backward(40)

t.forward(20)
t.right(90)
t.forward(20)
t.backward(40)


t.shape("circle")
t.penup()
t.forward(20)

#Drawing the pole
t.left(15)
t.forward(120)
t.left(120)
t.color("saddlebrown")
t.pensize(10)
t.pendown()
t.forward(350)

#Drawing the stand
t.begin_fill()
t.fillcolor("black")
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(200)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.end_fill()


t.hideturtle()
turtle.done()
