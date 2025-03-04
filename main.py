import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")

t = turtle.Turtle()
t.speed(0)

#check if it's in the right place
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.pensize(10)
# t.dot()
# t.pensize(1)

#square
t.setheading(135)
t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor("cyan")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.penup()

#square
t.setheading(45)
t.penup()
t.goto(0,0)
t.pendown()
t.fillcolor("Brown")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
t.penup()

t.hideturtle()
























































































turtle.done()