import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")


t = turtle.Turtle()
t.speed(0)
t.penup()

#circle
t.goto(-80,15)
t.pendown()
t.setheading(0)
t.pencolor("Blue")
t.circle(35)
t.penup()

t.goto(0,15)
t.pendown()
t.setheading(0)
t.pencolor("Black")
t.circle(35)
t.penup()

t.goto(80,15)
t.pendown()
t.setheading(0)
t.pencolor("Red")
t.circle(35)
t.penup()

t.goto(-40,-15)
t.pendown()
t.setheading(0)
t.pencolor("yellow")
t.circle(35)
t.penup()

t.goto(40,-15)
t.pendown()
t.setheading(0)
t.pencolor("green")
t.circle(35)
t.penup()

t.pencolor("purple")
t.penup()
t.goto(-5,100)
t.pendown()
t.write("Winter Olympics",font=("Arial",40,"bold italic"),align="center")

t.penup()
t.goto(0,-85)
t.pendown()
t.write("2026",font=("Arial",40,"bold italic"),align="center")



turtle.done()